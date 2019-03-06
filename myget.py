#!/usr/bin/python3
#coding:utf-8
# tested in win
# Version: 20190306

# bug 404 forbidden

import sys , os , shutil ,datetime , math
from urllib.parse import urlparse
from urllib import error
import urllib.request as req

# customized module
from mytool import mywait

def get_console_width():
    #Code from http://bitbucket.org/techtonik/python-pager
    if os.name == 'nt':
        STD_INPUT_HANDLE  = -10
        STD_OUTPUT_HANDLE = -11
        STD_ERROR_HANDLE  = -12
        # get console handle
        from ctypes import windll, Structure, byref
        from ctypes.wintypes import SHORT, WORD, DWORD
        console_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        # CONSOLE_SCREEN_BUFFER_INFO Structure
        class COORD(Structure):
            _fields_ = [("X", SHORT), ("Y", SHORT)]
        class SMALL_RECT(Structure):
            _fields_ = [("Left", SHORT), ("Top", SHORT),
                        ("Right", SHORT), ("Bottom", SHORT)]
        class CONSOLE_SCREEN_BUFFER_INFO(Structure):
            _fields_ = [("dwSize", COORD),
                        ("dwCursorPosition", COORD),
                        ("wAttributes", WORD),
                        ("srWindow", SMALL_RECT),
                        ("dwMaximumWindowSize", DWORD)]
        sbi = CONSOLE_SCREEN_BUFFER_INFO()
        ret = windll.kernel32.GetConsoleScreenBufferInfo(
            console_handle, byref(sbi))
        if ret == 0:
            return 0
        return sbi.srWindow.Right+1
    return 80

def filename_from_url(url):
    fname = os.path.basename(urlparse(url).path)
    if len(fname.strip(" \n\t.")) == 0:
        return None
    return fname

def pbar(blocks, block_size, total_size):
    if not total_size or total_size < 0:
        sys.stdout.write(str(block_size*blocks)+'\r')
    else:
        dlsize = block_size*blocks
        if dlsize > total_size: dlsize = total_size
        rate = dlsize/total_size
        percentrate = str(math.floor(100*rate))+'%'  
        width = int(get_console_width()/2-18)
        # print(width)
        # width = 40
        dots = int(math.floor(rate*width))
        # print(dots)
        bar = '▇'*dots+'--'*(width-dots)
        if total_size > (1024*1024):
            ts = str(total_size/(1024*1024))[:4]
            ds = str(dlsize/(1024*1024))[:4]
            unit = 'MB'
        elif total_size > 1024:
            ts = str(total_size/1024)[:4]
            ds = str(dlsize/1024)[:4]
            unit = 'KB' 
        else:
            ts = str(total_size)
            ds = str(dlsize) 
            unit = 'B'          
        e = '\n' if rate == 1 else '\r'
        sys.stdout.write(bar+' '+percentrate+' '+ds+'/'+ts+unit+e)
    sys.stdout.flush()

def dl(url,out=None,pbar=pbar):    
    # use pbar = None to supress process bar
    # detect of out is a directory
    outdir = None
    if out and os.path.isdir(out):
        outdir = out
        out = None

    fn = out if out else filename_from_url(url)
    if os.path.exists(fn):
        print('Already download --> Pass')
    else:
        now = str(datetime.datetime.utcnow()).replace(':','')
        tmpname = fn+now+'.tmp'   
        # opener = req.build_opener()
        # opener.addheaders = [('user-agent','Mozilla/5.0')]
        # req.install_opener(opener)
        try:
            local_filename, headers = req.urlretrieve(url,tmpname,pbar )
        except error.ContentTooShortError as e:
            mywait(5)
            local_filename, headers = req.urlretrieve(url,tmpname,pbar )
        # print(headers)
        # size = int(headers['Content-Length'])
        # ftype = '.'+str(headers['Content-Type']).split('/')[1]
        shutil.move(tmpname,out) if out else shutil.move(tmpname,fn)
 


if __name__ == "__main__":
    # url = 'http://python.org/'
    # url = 'https://github.com/hfaran/progressive/blob/master/example.gif'
    # url = 'http://m128.xiami.net/761/96761/2102654949/1795287087_1479699396518.mp3?auth_key=1546570800-0-0-c5bc8bc5db6fb85dde5e6171bd821a81'
    url = 'https://epass.icbc.com.cn/ICBCChromeExtension.msi'

    out = 'tesget.mp3'
    # out = None
    dl(url)
    # print(get_console_width())

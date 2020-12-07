#!/usr/bin/python3
#coding:utf-8
# tested in win

__version__ = 20200327

# bug 404 forbidden

'''
Module for common web crawling operaton
'''

import sys , os , shutil ,datetime , math
import requests
from urllib.parse import urlparse
from urllib import error
import urllib.request as req
# from concurrent import futures as cf
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from tenacity import *

# customized module
from mytool import mywait


def get_console_width():
    '''Get width of console'''
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
    '''Get file name from url'''
    fname = os.path.basename(urlparse(url).path)
    if len(fname.strip(" \n\t.")) == 0:
        return None
    return fname


def pbar(blocks, block_size, total_size):
    '''Progress bar for file downloading'''
    if not total_size or total_size < 0:
        sys.stdout.write(str(block_size*blocks)+'\r')
    else:
        dlsize = block_size*blocks
        if dlsize > total_size: dlsize = total_size
        rate = dlsize/total_size
        percentage = str(math.floor(100*rate))+'%'  
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
        sys.stdout.write(bar+' '+percentage+' '+ds+'/'+ts+unit+e)
    sys.stdout.flush()

@retry(
    stop=(stop_after_delay(10)|stop_after_attempt(5)),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(error.ContentTooShortError)
    )
def dl(url,out=None,pbar=pbar):
    '''Download file with progress bar by using urllib   
    use pbar = None to supress process bar
    '''
    # detect if out is a directory
    outdir = None
    if os.path.isdir(out):
        outdir = out # not change dir?
        out = None
    fn = out if out else filename_from_url(url)
    if not os.path.exists(fn):
        now = str(datetime.datetime.utcnow()).replace(':','')
        tmpname = fn+now+'.tmp'   
        try:
            local_filename, headers = req.urlretrieve(url,tmpname,pbar )
        except error.ContentTooShortError as e:
            print(e)
        except error.ConnectionResetError as e:
            print(e)
        shutil.move(tmpname,out) if out else shutil.move(tmpname,fn)

# def dl(url,out=None,pbar=pbar):
#     '''Download file with progress bar by using urllib   
#     use pbar = None to supress process bar
#     '''
#     # detect of out is a directory
#     outdir = None
#     if out and os.path.isdir(out):
#         outdir = out
#         out = None

#     fn = out if out else filename_from_url(url)

#     if os.path.exists(fn):
#         return f'{fn} --> Already download'
#     else:
#         now = str(datetime.datetime.utcnow()).replace(':','')
#         tmpname = fn+now+'.tmp'   
#         # opener = req.build_opener()
#         # opener.addheaders = [('user-agent','Mozilla/5.0')]
#         # req.install_opener(opener)
#         try:
#             local_filename, headers = req.urlretrieve(url,tmpname,pbar )
#         except error.ContentTooShortError as e:
#             mywait(5)
#             local_filename, headers = req.urlretrieve(url,tmpname,pbar )
#         # print(headers)
#         # size = int(headers['Content-Length'])
#         # ftype = '.'+str(headers['Content-Type']).split('/')[1]
#         shutil.move(tmpname,out) if out else shutil.move(tmpname,fn)


# def simpledl(file_url,folder='',file_name:str='',verify:bool=True):
#     '''download file by using requests
#     open in binary mode, no progress bar
#     '''
#     if file_name == '':
#         file_name = file_url.split('/')[-1]
#     if folder != '':
#         fullpath = os.path.join(folder,file_name)
#     else:
#         fullpath = file_name
#     # print(fullpath)
#     if os.path.exists(fullpath):
#         return False
#     try:
#         response = requests.get(file_url,verify=verify,timeout=100)             # get request
#     except requests.exceptions.ConnectionError as e:
#         # print(e)
#         mywait(2)
#         try:
#             response = requests.get(file_url,verify=verify,timeout=100) 
#         except:
#             raise
#     with open(fullpath, "wb") as f:
#         f.write(response.content)             # write to file

@retry(
    stop=(stop_after_delay(10)|stop_after_attempt(5)),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(requests.exceptions.ConnectionError)
    )
def simpledl(file_url,folder='',file_name:str='',verify:bool=True,headers=None):
    '''download file by using requests
    open in binary mode, no progress bar
    '''
    if not file_name:
        file_name = file_url.split('/')[-1]
    if folder:
        fullpath = os.path.join(folder,file_name)
    else:
        fullpath = file_name
    if os.path.exists(fullpath):
        return False
    try:
        response = requests.get(file_url,verify=verify,timeout=100,headers=headers)             # get request
    except requests.exceptions.ConnectionError as e:
        print(e)
    with open(fullpath, "wb") as f:
        f.write(response.content)   


# def download_cfmap(pic_list,ppath):
#     workers = min(MAX_WORKERS,len(pic_list))
#     with cf.ThreadPoolExecutor(workers) as ex:
#         ex.map(download,pic_list,timeout=60)

def download_cf(link_list,ppath,file_name='',maxworkers=10):
    '''Concurrent.future download'''
    workers = min(maxworkers,len(link_list))
    with ThreadPoolExecutor(workers) as ex:
        to_do = [ ex.submit(simpledl,link,ppath,file_name) for link in link_list ]
        done_iter = as_completed(to_do)
        list(tqdm(done_iter,total=len(to_do),bar_format='{n_fmt}/{total_fmt} {l_bar}'))

if __name__ == "__main__":
    # url = 'http://python.org/'
    # url = 'https://github.com/hfaran/progressive/blob/master/example.gif'
    # url = 'http://m128.xiami.net/761/96761/2102654949/1795287087_1479699396518.mp3?auth_key=1546570800-0-0-c5bc8bc5db6fb85dde5e6171bd821a81'
    url = 'https://epass.icbc.com.cn/ICBCChromeExtension.msi'
    url = 'https://www.sximg.com/u/20190517/04141852.jpg'
    out = 'tesget.jpg'
    # out = None
    simpledl(url)
    # print(get_console_width())

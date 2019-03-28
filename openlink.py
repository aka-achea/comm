#!/usr/bin/python3
#coding:utf-8
# Version: 20190328
# tested in win

import random,time,requests,sys
from urllib.request import urlopen,Request,HTTPError
from urllib.error import URLError

# customized module
from mytool import mywait

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml; " \
        "q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"text/html",
    "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }


def op_simple(URL): # use built-in
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml; " \
            "q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"text/html",
        "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        "Content-Type":"application/x-www-form-urlencoded",
        # "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 "\
        #     "(KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        #"Referer":"www.xiami.com"
        }
    req = Request(URL,headers=headers)
    try:
        html = urlopen(req)
        sys.stdout.write('Wait'+'\r')
        time.sleep(random.uniform(2,4))
        sys.stdout.write('    '+'\r')
        #l.verbose(html.info())
        #l.debug(html.getcode())
        status = html.getcode()
    except HTTPError as e:
        status = e #5xx,4xx
        html = 0
    except URLError as e:
        print('Host no response, try again')
        mywait(30)
        try:
            html = urlopen(req)
        except:
            status = e 
            html = 0
    return html,status #return array object

def op_sel(URL):     # use selenium
    pass

def op_requests(url,para='',verify=False):  # use requets
    try:
        html = requests.get(url=url,params=para,headers=headers,verify=verify,timeout=60)
    except requests.exceptions.ReadTimeout as e:
        return e
    except requests.exceptions.ConnectionError as e:
        print(e)
        return e
        # html.content
    return html



if __name__=='__main__':

    url = 'http://www.xiami.com/widget/xml-single/sid/1769402049'
    html = op_simple(url)
    print(html[1])
    print(html[0])

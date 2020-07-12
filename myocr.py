#!/usr/bin/python3
#coding:utf-8

__version__ = 20200223

from configparser import ConfigParser
from aip import AipOcr


def init_client():
    '''Initiate Baidu OCR Api'''
    confile = r'N:\GH\_pri\baidu.ini'
    config = ConfigParser()
    config.read(confile)
    APP_ID = config.get('BaiduOcr','APP_ID') 
    API_KEY = config.get('BaiduOcr','API_KEY')
    SECRET_KEY = config.get('BaiduOcr','SECRET_KEY')
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client


def ocr_baidu(client,image):
    '''Baidu basic Accurate OCR'''
    options = {
                "language_type":"CHN_ENG",
                "detect_direction":"true",
                "detect_language":"true",
                "probability":"true"
                }
    result = client.basicAccurate(image, options)
    # pprint(result)
    try:
        txtlist = [ x['words'] for x in result['words_result'] ]
    # pprint(txt)
    except:
        errcode = result['error_code']
        err = result['error_msg']
        raise SystemExit(errcode,err)
    return txtlist


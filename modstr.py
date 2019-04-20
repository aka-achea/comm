#!/usr/bin/python3
#coding:utf-8
#tested in win
# version: 20190420

import sys

from mylog import mylogger,get_funcname


if sys.platform == 'win32':
    logfile = 'E:\\app.log'
else:
    logfile = 'app.log'


def modificate(text):
    ml = mylogger(logfile,get_funcname)     
    #file_name = re.sub(r'\s*:\s*', u' - ', file_name)    # for FAT file system
    text = str(text)    
    before = text
    text = text.replace('?', u'？')      # for FAT file system
    text = text.replace('/', u'／')
    text = text.replace('|', '')
    text = text.replace(':', u'∶')    # for FAT file system
    text = text.replace('*', u'×')
    text = text.replace('&amp;', u'&')
    text = text.replace('&#039;', u'\'')
    #text = text.replace('\'', u'＇')
    text = text.replace('\\', u'＼')
    text = text.replace('"', u'＂')
    #text = text.replace('\'', u'＇')
    text = text.strip()
    #file_name = file_name.replace('$', '\\$')    # for command, see issue #7
    after = text
    if before != after :
        ml.debug("Before modify: "+before)
        ml.debug("After modify: "+after)
    return text

if __name__=='__main__':
    text1 = 'ル・デ'
    modificate(text1)
    print(text1)
   
   
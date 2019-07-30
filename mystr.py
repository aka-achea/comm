#!/usr/bin/python3
#coding:utf-8
#tested in win
#version: 20190730

'''
Module for processing string
'''

import sys

from mylog import mylogger,get_funcname


if sys.platform == 'win32':
    logfile = 'E:\\app.log'
else:
    logfile = 'app.log'



def batchremovestr(tlist,text):
    '''Remove words in tlist from text'''
    for t in tlist:
        text = text.replace(t,'')
    return text.strip()


def fnamechecker(text)->str:
    '''Replace reserved charactor in Windows path with other UTF8 charactor'''
    ml = mylogger(logfile,get_funcname()) 
    #file_name = re.sub(r'\s*:\s*', u' - ', file_name)    # for FAT file system
    before = text
    tlist = [('?', u'？'),('/', u'／'),('|', ''),(':', u'∶'),('*', u'×'),
                ('\n', ''),('\\', u'＼'),('"', u'＂')]
    #text = text.replace('\'', u'＇')
    for t,n in tlist:
        text = text.replace(t,n)
    text = text.strip()
    #file_name = file_name.replace('$', '\\$')    # for command, see issue #7
    after = text
    if before != after :
        ml.debug(f'{before} --> {after}')
    return text


def remove_emptyline(text):
    '''Remove empty line from paragraph''' 
    ntext = []
    for t in text.split('\n'):
        if t != '' and t != ' ':
            ntext.append(t)
    # print(text)
    return '\n'.join(ntext)


def remove_emptyline_file(f)->str:
    '''???Remove emptyline in file'''
    r_file = open(f, "r")
    lines = r_file.readlines()
    r_file.close()
    for idx, line in enumerate(lines):
        if line.split():
            print(idx, line)



if __name__=='__main__':
    text1 = 'ル・デ'
    fnamechecker(text1)
    print(text1)
   
   
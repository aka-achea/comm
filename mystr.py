#!/usr/bin/python3
#coding:utf-8
#tested in win
#version: 20190804

'''
Module for processing string
'''

import sys

from mylog import mylogger,get_funcname


if sys.platform == 'win32':
    logfile = 'E:\\app.log'
else:
    logfile = 'app.log'



def batchremovestr(tlist:list,text):
    '''Remove words in tlist from text'''
    for t in tlist:
        text = text.replace(t,'')
    return text.strip()


def batchreplacestr(tlist:list,text):
    '''Replace words in text against tuple list'''
    for t,n in tlist:
        text = text.replace(t,n)
    return text.strip()    


def fnamechecker(text)->str:
    '''Replace reserved charactor in Windows path with other UTF8 charactor'''
    tlist = [('?', u'？'),('/', u'／'),('|', ''),(':', u'∶'),('*', u'×'),
                ('\n', ''),('\\', u'＼'),('"', u'＂')]    
    return batchreplacestr(tlist,text)


# def fnamechecker(text)->str:
#     '''Replace reserved charactor in Windows path with other UTF8 charactor'''
#     ml = mylogger(logfile,get_funcname()) 
#     #file_name = re.sub(r'\s*:\s*', u' - ', file_name)    # for FAT file system
#     before = text
#     tlist = [('?', u'？'),('/', u'／'),('|', ''),(':', u'∶'),('*', u'×'),
#                 ('\n', ''),('\\', u'＼'),('"', u'＂')]
#     #text = text.replace('\'', u'＇')
#     for t,n in tlist:
#         text = text.replace(t,n)
#     text = text.strip()
#     #file_name = file_name.replace('$', '\\$')    # for command, see issue #7
#     after = text
#     if before != after :
#         ml.debug(f'{before} --> {after}')
#     return text


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


def remove_dupline(file):
    '''Remove duplicate line in the file (UTF8)'''
    pass
#     with open(file,'r',encoding='utf-8') as f:
#         lines = f.readlines()
#         newlines = { for l in lines}


def splitall(seplist,text):
    for sep in seplist:
        text = text.replace(sep,',')
    return [x for x in text.split(',') if x]


if __name__=='__main__':
    # text1 = 'ル・デ'
    text = '发行时间：2019-06-23'
    seplist = ['：','-']
    r = splitall(seplist, text)
    print(r)
   

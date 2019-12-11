#!/usr/bin/python3
#coding:utf-8
#tested in win
__version__ = 20191207

'''
Module for processing string
'''

import sys,os

from mylog import mylogger,get_funcname


if sys.platform == 'win32':
    logfile = 'E:\\app.log'
else:
    logfile = 'app.log'



def batchremovestr(tlist:list,text):
    '''Remove word in text list from text'''
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
                ('\n', ''),('\\', u'＼'),('"', u'＂'),('\t',' ')]    
    return batchreplacestr(tlist,text)


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
    os.rename(file,file+'.old') 
    with open(file+'.old','r',encoding='utf-8') as f:
        lines = f.readlines()
        newlines = { line for line in lines }
    with open(file,'w',encoding='utf-8') as f:
        f.writelines(newlines)


def splitall(seplist,text):
    '''Split text from seplist'''
    for sep in seplist:
        text = text.replace(sep,',')
    return [x for x in text.split(',') if x]


if __name__=='__main__':
    # text1 = 'ル・デ'
    t = r'L:\movie.txt'
    remove_dupline(t)
   

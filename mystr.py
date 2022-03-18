#!/usr/bin/python3
#coding:utf-8
#tested in win

__version__ = 20200328

'''
Module for processing string
'''

import sys,os


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


def remove_dupline(filename):
    '''Remove duplicate line in the file (UTF8)'''
    if os.path.exists(filename+'.old'):
        os.remove(filename+'.old')
    os.rename(filename,filename+'.old') 
    with open(filename+'.old','r',encoding='utf-8') as f:
        lines = f.readlines()
    newlines = set(lines)
    with open(filename,'w',encoding='utf-8') as f:
        for x in newlines:
            f.write(x)



def splitall(seplist,text):
    '''Split text from seplist'''
    for sep in seplist:
        text = text.replace(sep,',')
    return [x for x in text.split(',') if x]


def dedupe(items, key=None):
    '''dedup from a sequence while maintain order'''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
    return seen


def filterstart(file,start):
    from itertools import dropwhile
    with open(file) as f:
        for line in dropwhile(lambda line: line.startswith(start),f):
            print(line,end='')



def merge_file(f1,f2,outfile):
    '''f1,f2 need sorted first'''
    import heapq
    with open(f1, 'rt') as file1, \
        open(f2, 'rt') as file2, \
        open(outfile, 'wt') as outf:
        for line in heapq.merge(file1, file2):
            outf.write(line)


def remove_comment(file):
    '''Remove comment #'''
    import itertools
    with open(file,'r') as f:
        string = f.readlines
        for x in itertools.dropwhile(lambda line:line.startswith("#"), f.split("\n")): 
            print(x)


if __name__=='__main__':
    # text1 = 'ル・デ'
    t = r'L:\movie.txt'
    # remove_dupline(t)



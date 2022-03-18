#!/usr/bin/python3
#coding:utf-8
# tested in win
__version__ = 20200130

'''
Module for file common operation
'''

import shutil
import os
from fnmatch import fnmatch
import json
from os import listdir
from os.path import join as pjoin
from os.path import isdir as pisdir
from os.path import isfile as pisfile
from os.path import exists as pexists


def g_dsize(folderpath): 
    '''get folder total size'''
    size = 0
    for root, dirs, files in os.walk(folderpath):
        size += sum([os.path.getsize(pjoin(root, name)) for name in files])
    return size


def g_fsize(folderpath,excludelist=['SRT','HTM','ENT','2TS']): 
    '''get all file size dict\n
    default excluding *.srt,htm,ent,2ts
    '''
    adict = {}
    for root, dirs, files in os.walk(folderpath):
        for name in files:
            if name[-3:].upper() not in excludelist: 
                adict[name.upper()] = os.path.getsize(pjoin(root, name))
    return adict


def d_move(src,dstparent):
    '''Move src folder under dst folder, if exist then compare/remove'''
    # dst = pjoin(parent,src.split('\\')[-1])
    dst = pjoin(dstparent,os.path.split(src)[1])
    if os.path.exists(dst):
        ds = g_dsize(dst)/(1024*1024) #MB
        ss = g_dsize(src)/(1024*1024)
        # print('DST: '+str(ds))
        # print('SRC: '+str(ss))
        if ds < ss:
            shutil.rmtree(dst)
            shutil.move(src,dstparent) 
            return f'Replace small one {dst}'
        else:
            shutil.rmtree(src)
            return f"Already have big one {dst}"
    else:
        shutil.move(src,dstparent)
        return f'Move folder to {dst}'


def f_move(src,dst):
    '''Move/Rename file from SRC to DST'''
    if os.path.exists(dst) and src != dst:
        # print('DST: '+str(os.path.getsize(dst)))
        # print('SRC: '+str(os.path.getsize(src)))
        if os.path.getsize(dst) < os.path.getsize(src):
            os.remove(dst)
            shutil.move(src,dst)
            return f'Replace small one {dst}'
        else:
            os.remove(src)
            return f"Already have big one {dst}"
    else:
        shutil.move(src,dst)
        return f'Move file to {dst}'


def batch_rename(folderpath,oldcharactor,newcharactor):  
    '''Batch replace file name charactor in folder'''
    for f in listdir(folderpath):
        fp = pjoin(folderpath,f)
        if pisfile(fp):
        # print(pjoin(folderpath,f[:-4]+'c.jpg'))
            nf = f.replace(oldcharactor,newcharactor)
            os.rename(fp,pjoin(folderpath,nf))


def ucase(folderpath):
    '''Upper name all file in folder'''
    for f in listdir(folderpath):
        nfile = f.upper()
        if nfile != f :        
            src = pjoin(folderpath,f)        
            dst = pjoin(folderpath,nfile)        
            shutil.move(src,dst)


def comparedir(question,baseline):
    '''Compare file in question folder and baseline folder'''
    return set(listdir(question))&set(listdir(baseline))     


def clean_f(path,suffix):
    '''Clean File with specified suffix'''
    for f in listdir(path):
        if fnmatch(f,'*.'+suffix):
            os.remove(f)


def count_f(path,suffix):
    '''Count file with specified suffix'''
    c = 0
    for f in listdir(path):        
        if fnmatch(f,'*.'+suffix): 
            c += 1
    return c
                

def jdump(outfile,data):
    '''Save json data to outfile'''
    with open(outfile,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)


def jload(infile):
    '''Load json data from infile'''
    with open(infile,'r',encoding='utf-8') as f:
        j = json.loads(f.read())
    return j

if __name__ == "__main__":
    p = r'D:\DL\_'
    # batch_rename(p,'纪元','')    
    print(g_dsize(p))
    
#!/usr/bin/python3
#coding:utf-8
# tested in win
# version: 20190730

'''
Module for file common operation
'''

import shutil
import os
import fnmatch


def g_dsize(folderpath): 
    '''get folder total size'''
    size = 0
    for root, dirs, files in os.walk(folderpath):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def d_move(src,dstparent):
    '''Move src folder under dst folder, if exist then compare/remove'''
    # dst = os.path.join(parent,src.split('\\')[-1])
    dst = os.path.join(dstparent,os.path.split(src)[1])
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
    for f in os.listdir(folderpath):
        fp = os.path.join(folderpath,f)
        if os.path.isfile(fp):
        # print(os.path.join(folderpath,f[:-4]+'c.jpg'))
            nf = f.replace(oldcharactor,newcharactor)
            os.rename(fp,os.path.join(folderpath,nf))


def ucase(folderpath):
    '''Upper name all file in folder'''
    for f in os.listdir(folderpath):
        nfile = f.upper()
        if nfile != f :        
            src = os.path.join(folderpath,f)        
            dst = os.path.join(folderpath,nfile)        
            shutil.move(src,dst)


def comparedir(question,baseline):
    '''Compare file in question folder and baseline folder'''
    return set(os.listdir(question))&set(os.listdir(baseline))     


def clean_f(path,suffix):
    '''Clean File with specified suffix'''
    for f in os.listdir(path):
        if fnmatch.fnmatch(f,'*.'+suffix):
            os.remove(f)


def count_f(path,suffix):
    '''Count file with specified suffix'''
    c = 0
    for f in os.listdir(path):        
        if fnmatch.fnmatch(f,'*.'+suffix): 
            c += 1
    return c
                


if __name__ == "__main__":
    p = r'E:\AWS training 2019'
    # re_file(p,'JPEG','jpg')    
    print(g_dsize(p))
    
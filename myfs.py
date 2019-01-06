#!/usr/bin/python
#coding:utf-8
# Python3
# version: 20181230

import shutil,os

def g_dsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def d_move(src,parent): #move folder , folder itself don't exist
    dst = os.path.join(parent,src.split('\\')[-1])
    if os.path.exists(dst):
        ds = g_dsize(dst)/(1024*1024) #MB
        ss = g_dsize(src)/(1024*1024)
        print('DST: '+str(ds))
        print('SRC: '+str(ss))
        if ds < ss:
            print('Replace small one')
            shutil.rmtree(dst)
            shutil.move(src,parent) 
        else:
            print("Already have big one")
            shutil.rmtree(src)
    else:
        shutil.move(src,parent)

def f_move(src,dst):
    if os.path.exists(dst) and src != dst:
        print(dst)
        print('DST: '+str(os.path.getsize(dst)))
        print('SRC: '+str(os.path.getsize(src)))
        if os.path.getsize(dst) < os.path.getsize(src):
            print('Replace small one')
            os.remove(dst)
            shutil.move(src,dst)
        else:
            print("Already have big one")
            os.remove(src)
    else:
        shutil.move(src,dst)



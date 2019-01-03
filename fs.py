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

def d_move(src,dst): 
    if os.path.exists(dst):
        ds = g_dsize(dst)
        ss = g_dsize(src)
        print('DST: '+ds)
        print('SRC: '+ss)
        if ds < ss:
            print('Replace small one')
            shutil.rmtree(dst)
            shutil.move(src,dst) 
        else:
            print("Already have big one")
            shutil.rmtree(src)
    else:
        shutil.move(src,dst)

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



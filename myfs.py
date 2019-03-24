#!/usr/bin/python3
#coding:utf-8
# tested in win
# version: 20190324

import shutil
import os

def g_dsize(dir): #get dir size
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def d_move(src,parent): #move folder 
    # dst = os.path.join(parent,src.split('\\')[-1])
    dst = os.path.join(parent,os.path.split(src)[1])
    if os.path.exists(dst):
        ds = g_dsize(dst)/(1024*1024) #MB
        ss = g_dsize(src)/(1024*1024)
        # print('DST: '+str(ds))
        # print('SRC: '+str(ss))
        if ds < ss:
            shutil.rmtree(dst)
            shutil.move(src,parent) 
            result = f'Replace small one {dst}'
        else:
            shutil.rmtree(src)
            result = f"Already have big one {dst}"
    else:
        shutil.move(src,parent)
        result = f'Move folder to {dst}'
    return result

def f_move(src,dst):
    if os.path.exists(dst) and src != dst:
        # # print(dst)
        # print('DST: '+str(os.path.getsize(dst)))
        # print('SRC: '+str(os.path.getsize(src)))
        if os.path.getsize(dst) < os.path.getsize(src):
            os.remove(dst)
            shutil.move(src,dst)
            result = f'Replace small one {dst}'
        else:
            os.remove(src)
            result = f"Already have big one {dst}"
    else:
        shutil.move(src,dst)
        result = f'Move file to {dst}'
    return result

def re_file(p,old,new):    
    for f in os.listdir(p):
        fp = os.path.join(p,f)
        if os.path.isfile(fp):
        # print(os.path.join(p,f[:-4]+'c.jpg'))
            nf = f.replace(old,new)
            os.rename(fp,os.path.join(p,nf))


if __name__ == "__main__":
    p = r'L:\Music\_5s'
    re_file(p,'JPEG','jpg')    
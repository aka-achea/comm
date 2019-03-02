#!/usr/bin/python3
#coding:utf-8
# tested in win
# version: 20190302

import shutil,os

def g_dsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def d_move(src,parent): #move folder , folder itself don't exist
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
            result = 'Replace small one'
        else:
            shutil.rmtree(src)
            result = "Already have big one"
    else:
        shutil.move(src,parent)
        result = 'Move folder'
    return result

def f_move(src,dst):
    if os.path.exists(dst) and src != dst:
        # # print(dst)
        # print('DST: '+str(os.path.getsize(dst)))
        # print('SRC: '+str(os.path.getsize(src)))
        if os.path.getsize(dst) < os.path.getsize(src):
            os.remove(dst)
            shutil.move(src,dst)
            result = 'Replace small one'
        else:
            os.remove(src)
            result = "Already have big one"
    else:
        shutil.move(src,dst)
        result = 'Move file'
    return result


if __name__ == "__main__":
    src = r'M:\迅雷下载'
    parent = r'M:\webproject'    
    d_move(src,parent)
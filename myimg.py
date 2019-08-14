#!/usr/bin/python3
#coding:utf-8
# tested in win
#version 20190730

'''
Module for image/video process
'''


from PIL import Image
import imageio
import numpy as np
import os


def gifsplit(gif,outfolder):
    '''Split GIF to PNG'''
    images = imageio.mimread(gif)
    #把上面的每帧图片进行保存
    for x, img in enumerate(images):
        img = np.asarray(img)
        imageio.imwrite(os.path.join(outfolder,"%d.png" % x), img)


def gifmake(folder,gifname):
    '''Make GIF from PNG in folder'''
    fileOrder = sorted([int(os.path.splitext(x)[0]) for x in os.listdir(folder)])
    # print(fileOrder)
    frames = []
    for order in fileOrder:
        filePath = os.path.join(folder,str(order)+'.png')
        frames.append(imageio.imread(filePath))
    gifpath = os.path.join(folder,gifname)
    imageio.mimsave(gifpath, frames, 'GIF', duration = 0.1)


def imgresize(pic,pix):
    '''Resize Image to specified pix'''
    img = Image.open(pic)   
    return img.resize((pix,pix),Image.LANCZOS)



if __name__ == "__main__":
    pic = r'M:\MyProject\ocr\t.gif'
    outfolder = r'M:\MyProject\ocr'
    # gifsplit(pic,outfolder)
    gifname = 'g.gif'
    gifmake(outfolder,gifname)
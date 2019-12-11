#!/usr/bin/python3
#coding:utf-8
# tested in win
#version 20190818

'''
Module for image/video process
'''


from PIL import Image
import imageio
import numpy as np
import os


base = np.array([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],  ])

heart = np.array([
    [0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0], ])

C = np.array([
    [0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0],  ])

E = np.array([
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0],  ])

H = np.array([
    [0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,0,0,0,0,0],  ])

I = np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],  ])

L = np.array([
    [0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0],  ])

O = np.array([
    [0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0],  ])

R = np.array([
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,1,1,1,0,0],
    [0,1,0,1,0,0,0],
    [0,1,0,0,1,0,0],
    [0,1,0,0,0,1,0],
    [0,0,0,0,0,0,0],  ])

U = np.array([
    [0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0],  ])

V = np.array([
    [0,0,0,0,0,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,1,0,1,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0],  ])

zeorarr = np.zeros(( len(base),1 )) # for concatenate array

mapdic = { 'C':C,'E':E,'H':H,'I':I,'L':L,'O':O,'R':R,'U':U,'V':V }


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


# def imgresize(pic,pix):
#     '''Resize Image to specified pix'''
#     img = Image.open(pic)   
#     return img.resize((pix,pix),Image.LANCZOS)


def squaresize(pic,size=50):
    '''Crop a squar and resize'''
    img = Image.open(pic)   
    width, height = img.size
    newsize = width if width < height else height 
    left = (width - newsize)/2
    top = (height - newsize)/2
    right = (width + newsize)/2
    bottom = (height + newsize)/2
    img.crop((left, top, right, bottom))
    img = img.resize((size,size),Image.LANCZOS)
    return img


def pix2char(r,b,g,alpha=256):
    ''''''
    if alpha == 0:
        return ' '
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0+1)/len(ascii_char)
    return ascii_char[int(gray/unit)]


def pic2char(img):
    ''''''
    width,height = 300,300    
    img = Image.open(img)
    img = img.resize((width,height),Image.NEAREST)
    txt = ""
    for y in range(height):
        for x in range(width):
            txt += pix2char(*img.getpixel((x,y)))
        txt += '\n'
    print(txt)
    return txt


def figletter(word):  
    '''create geek letter'''
    import pyfiglet
    result = pyfiglet.figlet_format(str(word), font = "standard"  ) 
    print(result)
    return result








if __name__ == "__main__":
    pic = r'M:\MyProject\ocr\t.gif'
    outfolder = r'M:\MyProject\ocr'
    # gifsplit(pic,outfolder)
    gifname = 'g.gif'
    gifmake(outfolder,gifname)
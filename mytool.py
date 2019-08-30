#!/usr/bin/python3
#coding:utf-8
#tested in win
#version 20190827


'''
Module for misc tool
'''


import time,sys
import pyautogui as auto
import win32con
import win32clipboard as wincld


def mytimer(label='',trace=True):
    '''Timer decorator'''
    class Timer:
        def __init__(self,func):
            self.func = func
            self.alltime = 0
        def __call__(self,*args,**kargs):
            start = time.process_time()
            result = self.func(*args,**kargs)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__,elapsed,self.alltime)
                print( format % values )
            return result
    return Timer


def mywait(n):
    '''Wait for n seconds'''
    for i in range(n):
        space = 1 if (60-i) > 9 else 2
        sys.stdout.write('Wait'+' '*space+str(n-i)+'\r')
        time.sleep(1)


def combinekey(a,b):
    '''press two key'''
    auto.keyDown(a)
    auto.keyDown(b)
    auto.keyUp(a)
    auto.keyUp(b)


def capture(img,trys=10,confidence=0.9):  
    '''Find botton location'''  
    # pic = os.path.join(wp,img+'.png')
    trytime = 1
    while trytime < trys:
        try:
            button = auto.locateCenterOnScreen(img,grayscale=True,confidence=confidence)
            time.sleep(1)
            break            
        except TypeError:
            time.sleep(15)
            trytime += 1
            print(f'try to locate {img} {str(trytime)}')
            continue
        except OSError as e:
            print(e)
            return e
    else:
        print(f"Max tries reach, not able to locate option {img}")
        button = None
        # return f"Max tries reach, not able to locate option {img}"
        # raise(f'Find no {img}')
    return button


def clickbutton(img,**args):
    '''click button'''
    button = capture(img,**args)
    if isinstance(button,tuple):
        auto.click(button)
        return True
    else:
        return False


def get_text_clipboard():
    '''Get text from clipboard'''
    wincld.OpenClipboard()
    try:
        text_result = wincld.GetClipboardData(win32con.CF_UNICODETEXT)
    except TypeError:
        return None
    # wincld.EmptyClipboard()
    wincld.CloseClipboard()
    return text_result




if __name__ == "__main__":
    f = r'M:\GH\a.txt'
    remove_emptyline_file(f)
#!/usr/bin/python3
#coding:utf-8
#tested in win
# version 20190406

import time,sys


def mytimer(label='',trace=True):
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
    for i in range(n):
        space = 1 if (60-i) > 9 else 2
        sys.stdout.write('Wait'+' '*space+str(n-i)+'\r')
        time.sleep(1)

def remove_emptyline(text):
    a = text.split('\n')
    text = []
    for t in a:
        if t != '' and t != ' ':
            text.append(t)
    # print(text)
    text = '\n'.join(text)
    return text

def remove_emptyline_file(f):
    r_file = open(f, "r")
    lines = r_file.readlines()
    r_file.close()
    for idx, line in enumerate(lines):
        if line.split():
            print(idx, line)
        r_file.close()


if __name__ == "__main__":
    f = r'M:\GH\a.txt'
    remove_emptyline_file(f)
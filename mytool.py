#!/usr/bin/python
#coding:utf-8
# Python3


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
        sys.stdout.write('Wait'+' '*space+str(60-i)+'\r')
        time.sleep(1)


#!/usr/bin/python3
#coding:utf-8
#tested in win

from pprint import pprint
import inspect
import os
import logging
from colorama import Fore,Style,init
# from cmreslogging.handlers import CMRESHandler

__Version__ = 20200322

"""
CRITICAL50
ERROR   40
WARNING 30
INFO    20
DEBUG   10
NOTSET  0
"""


class mylogger():
    '''Log to file and console'''
    def __init__(self,logfile=None,funcname=None):
        init(autoreset=True)
        if logfile:
            self.logfile = logfile
            self.fh = logging.FileHandler(self.logfile,'a',encoding='utf-8')
            formatter = logging.Formatter(datefmt='%m-%d %H:%M:%S',fmt='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
            self.fh.setFormatter(formatter)
            self.logger = logging.getLogger(funcname)
            self.logger.setLevel('DEBUG')
            self.logger.addHandler(self.fh) 

    def debug(self,msg):
        # print(Fore.RED +Style.BRIGHT+ msg)
        if self.logfile: self.logger.debug(msg)
    
    def info(self,msg):
        print(Fore.GREEN +Style.BRIGHT+ msg)
        if self.logfile: self.logger.info(msg)

    def warn(self,msg):
        print(Fore.YELLOW +Style.BRIGHT+ msg)
        if self.logfile: self.logger.warning(msg)

    def err(self,msg):
        print(Fore.RED +Style.BRIGHT+ msg)
        if self.logfile: self.logger.error(msg)

    def critical(self,msg):
        print(Fore.MAGENTA +Style.BRIGHT+ msg)
        if self.logfile: self.logger.critical(msg)        


def get_funcname():
    # sys._getframe().f_code.co_name
    # sp = '\\' if sys.platform == 'win32' else '/'
    # pprint(inspect.stack()[1])
    func = inspect.stack()[1].function
    mod = inspect.stack()[1].filename
    mod = os.path.basename(mod).split('.')[0]
    lineno = str(inspect.stack()[1].lineno)
    mfl = '.'.join([mod,func,lineno])
    return mfl




if __name__=='__main__': #Usage
    import sys,os
    logfile = 'app.log'
    if sys.platform == 'win32':
        path = 'E:'
    else:
        path = '/var/log'
    logfile = os.path.join(path,logfile) 
    # logfilelevel = 10 # Debug
    
    # test mylogger
    # ml = mylogger(logfile)   
    # ml.debug('This is Debug')
    # a = 'ール・デ'
    # ml.info(a)
    # ml.err('error log')
    # ml.warn('warning log')
    # ml.critical("this is a critical message")
    # ml.verbose('vvvvv')

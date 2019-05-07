#!/usr/bin/python3
#coding:utf-8
#tested in win
# Version: 20190506

# CRITICAL    50
# ERROR   40
# WARNING 30
# INFO    20
# DEBUG   10
# NOTSET  0

"""
C:\Program Files\Python3.7.2\lib\logging\__init__.py
line 1037 add the following to fix \xa0 issue
    
        except UnicodeEncodeError:
            import unicodedata
            msg = unicodedata.normalize("NFKD",msg)
            stream.write(msg + self.terminator)
            self.flush()	

"""

import logging
import coloredlogs
import functools
import inspect
import unicodedata
import sys






levelmap = {
            #'debug': {'color': 'magenta','bold': True},
            'info': {'color': 'green','bold': True},
            'warning': {'color': 'yellow','bold': True},
            'error': {'color': 'red','bold': True},
            'critical': {'color': 'magenta','bold': True}
            }

def get_funcname():
    sp = '\\' if sys.platform == 'win32' else '/'
    func = inspect.stack()[1][3]
    mo = str(inspect.stack()[1][1]).split(sp)[-1].split('.')[0]
    # print(mo)
    mf = mo+'.'+func
    lineno = inspect.stack()[1][2]
    return mf
    
# experiment , not in use 
def logwrap(logfile):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # global l
            logfilelevel = 10
            l = mylogger(logfile,logfilelevel,func.__name__)
            print(l)
            print(func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

class mylogger():
    def __init__(self,logfile,funcname,logfilelevel=10):
        # logging.basicConfig(level=logfilelevel,filename=logfile,datefmt='%m-%d %H:%M:%S',
        #     format='%(asctime)s <%(name)s>[%(levelname)s] %(message)s')
        # logging.basicConfig(level=logfilelevel)
        fh = logging.FileHandler(logfile,'a',encoding='utf-8')
        formatter = logging.Formatter(datefmt='%m-%d %H:%M:%S',
            fmt='%(asctime)s <%(name)s>[%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logfilelevel)
        self.logger = logging.getLogger(funcname)
        self.logger.addHandler(fh) 
        # self.logger.propagate = False
        coloredlogs.DEFAULT_LEVEL_STYLES = levelmap 
        coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
        coloredlogs.install(level='info')  
        # coloredlogs.install(level='info',logger=self.logger)  

    def debug(self,msg):
        self.logger.debug(msg)
    def info(self,msg):
        self.logger.info(msg)
    def warning(self,msg):
        self.logger.warning(msg)
    def error(self,msg):
        self.logger.error(msg)
    def critical(self,msg):
        self.logger.critical(msg)
    def verbose(self,msg):
        self.logger.debug(msg)

class myconlog():
    def __init__(self):
        self.logger = logging.getLogger()
        # coloredlogs.DEFAULT_LEVEL_STYLES= {
        #                                 #'debug': {'color': 'magenta','bold': True},
        #                                 'info': {'color': 'green','bold': True},
        #                                 'warning': {'color': 'yellow','bold': True},
        #                                 'error': {'color': 'red','bold': True},
        #                                 'critical': {'color': 'magenta','bold': True}
        #                                     }
        coloredlogs.DEFAULT_LEVEL_STYLES = levelmap 
        coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
        coloredlogs.install(level='info')  
    def debug(self,msg):
        self.logger.debug(msg)
    def info(self,msg):
        self.logger.info(msg)
    def warning(self,msg):
        self.logger.warning(msg)
    def error(self,msg):
        self.logger.error(msg)
    def critical(self,msg):
        self.logger.critical(msg)
    def verbose(self,msg):
        self.logger.debug(msg)


class myfilelog():
    def __init__(self,logfile,logfilelevel=10):
        # logging.basicConfig(level=logfilelevel)
        self.fh = logging.FileHandler(logfile,'a',encoding='utf-8')
        formatter = logging.Formatter(datefmt='%m-%d %H:%M:%S',
            fmt='%(asctime)s <%(module)s-%(funcName)s-%(lineno)d>[%(levelname)s] %(message)s')
        self.fh.setFormatter(formatter)
        self.fh.setLevel(logfilelevel)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(self.fh) 
        self.logger.propagate = False  # disable log to parent handler

    def debug(self,msg):
        self.logger.debug(msg)
    def info(self,msg):
        self.logger.info(msg)
    def warning(self,msg):
        self.logger.warning(msg)
    def error(self,msg):
        self.logger.error(msg)
    def critical(self,msg):
        self.logger.critical(msg)
    def verbose(self,msg):
        self.logger.debug(msg)

    # def close(self):
    #     self.logger.removeHandler(self.fh)
        


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
    # ml = mylogger(logfile,get_funcname())   
    # ml.debug('This is Debug')
    # ml.info('ール・デ')
    # ml.error('error log')
    # ml.warning('warning log')
    # ml.critical("this is a critical message")
    # ml.verbose('vvvvv')

    # # test myconlog
    # ml = myconlog() 
    # ml.debug('This is Debug')
    # ml.info('ール・デ')
    # ml.error('error log')
    # ml.warning('warning log')
    # ml.critical("this is a critical message")
    # ml.verbose('vvvvv')


    # test myconlog
    ml = myfilelog(logfile) 
    ml.debug('This is Debug')
    ml.info('ール・デ')
    ml.error('error log')
    ml.warning('warning log')
    ml.critical("this is a critical message")
    ml.verbose('vvvvv')

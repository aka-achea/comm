#!/usr/bin/python3
#coding:utf-8
#tested in win
# Version: 20190302

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

import logging,coloredlogs,functools,inspect,unicodedata




def get_funcname():
    func = inspect.stack()[1][3]
    mo = str(inspect.stack()[1][1]).split('/')[-1].split('.')[0]
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
    def __init__(self,logfile,logfilelevel,funcname):
        logging.basicConfig(level=logfilelevel,filename=logfile,filemode='w',
                            datefmt='%m-%d %H:%M:%S',
                            format='%(asctime)s <%(name)s>[%(levelname)s] %(message)s')
        self.logger = logging.getLogger(funcname)
        coloredlogs.DEFAULT_LEVEL_STYLES= {
                                        #'debug': {'color': 'magenta','bold': True},
                                        'info': {'color': 'green','bold': True},
                                        'warning': {'color': 'yellow','bold': True},
                                        'error': {'color': 'red','bold': True},
                                        'critical': {'color': 'magenta','bold': True}
                                            }
        coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
        coloredlogs.install(level='info',logger=self.logger)  
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
        coloredlogs.DEFAULT_LEVEL_STYLES= {
                                        #'debug': {'color': 'magenta','bold': True},
                                        'info': {'color': 'green','bold': True},
                                        'warning': {'color': 'yellow','bold': True},
                                        'error': {'color': 'red','bold': True},
                                        'critical': {'color': 'magenta','bold': True}
                                            }
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


if __name__=='__main__': #Usage
    # funcname = __name__
    # logfilelevel = 10 # Debug
    # logfile = 'E:\\app.log'
    # l = mylogger(logfile,logfilelevel,funcname)   
    import sys
    
    if sys.platform == 'win32':
        logfile = 'E:\\app.log'
    else:
        logfile = 'app.log'
    l = myconlog()   

    l.debug('This is Debug')
    l.info('ール・デ')
    l.error('error log')
    l.warning('warning log')
    l.critical("this is a critical message")
    l.verbose('vvvvv')

#!/usr/bin/python3
#coding:utf-8
#tested in win

__version__ = 20200329

from inspect import signature
from functools import wraps
import time


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                        'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


def timethis(func):
    '''
    Decorator that reports the execution time. Usage:\n
    @timethis\n
    def FUNCTION():
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, round(end-start,5))
        return result
    return wrapper


# not working
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


import inspect
def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                    inspect.Parameter.KEYWORD_ONLY,
                                    default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


from functools import wraps, partial
import logging
def attach_wrapper(obj, func=None):  # Helper function that attaches function as attribute of an object
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func
def log(level, message):  # Actual decorator
    def decorate(func):
        logger = logging.getLogger(func.__module__)  # Setup logger
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        log_message = f"{func.__name__} - {message}"
        @wraps(func)
        def wrapper(*args, **kwargs):  # Logs the message and before executing the decorated function
            logger.log(level, log_message)
            return func(*args, **kwargs)
        @attach_wrapper(wrapper)  # Attaches "set_level" to "wrapper" as attribute
        def set_level(new_level):  # Function that allows us to set log level
            nonlocal level
            level = new_level
        @attach_wrapper(wrapper)  # Attaches "set_message" to "wrapper" as attribute
        def set_message(new_message):  # Function that allows us to set message
            nonlocal log_message
            log_message = f"{func.__name__} - {new_message}"
        return wrapper
    return decorate
    
# Example Usage
# @log(logging.WARN, "example-param")
# def somefunc(args):
#     return args
# somefunc("some args")
# somefunc.set_level(logging.CRITICAL)  # Change log level by accessing internal decorator function
# somefunc.set_message("new-message")  # Change log message by accessing internal decorator function
# somefunc("some args")
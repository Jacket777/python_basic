"""
9.1.5 装饰器自定义属性
"""

from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function, level is the logging level,
    name is the logger name, and message is the log message.
    If name and message aren't specified,they default to the function's module and name
    :param level:
    :param name:
    :param message:
    :return:
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__


        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(f'add result: {add(3,5)}')
    add.set_message('Add called')
    print(f'add result: {add(3,5)}')
    add.set_level(logging.WARNING)
    print(f'add result: {add(3, 5)}')


import functools
from logging import Logger
from time import time


def clock(writer: Logger = None):
    def decorated(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            elapsed_time = time() - start_time
            name = func.__name__
            args_str = ', '.join(repr(arg) for arg in args) \
                if args else 'None'
            kwargs_str = ', '.join("\'{}\'={}".format(key, repr(value)) for key, value in kwargs.items()) \
                if kwargs else 'None'
            message = 'Time: [%0.8fs] Function: %s (args=%s, kwargs={%s}) -> %r' % (
                    elapsed_time, name, args_str, kwargs_str, result)
            if not writer:
                print(message)
            else:
                writer.warning(message)
            return result
        return clocked
    return decorated

import timeit
import time
import random


'''
python im timeit -s "[ord(x) for x in 'abcdfghi']"
python -m timeit -s “[chr(int(x)) for x in ‘123456789’]”
'''


def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass


# python -m timeit “import simple_func; simple_func.my_function()”


def timefunc(func):
    '''
    A timer decorator
    '''
    def function_timer(*args, **kwargs):
        '''
        A nested function for timing other functions
        '''
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer


@timefunc
def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1, 5))
        time.sleep(sleep_time)


# create a timming context manager
class MyTimer():
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __eixt__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))


if __name__ == '__main__':
    # timeit for testing
    setup = "from __main__ import my_function"
    print(timeit.timeit('my_function()', setup=setup))
    long_runner()

    with MyTimer():
        long_runner()

import timeit
import math
from math import sin


def test1(x):
    return math.sin(x)


def test2(x):
    return sin(x)


def test3(x, sin=math.sin):
    return sin(x)


if __name__ == '__main__':
#    t1 = timeit.timeit('test1(123456)', 'from __main__ import test1',
#                       number=100000000)
#    print(t1 / 100000000)
#    t2 = timeit.timeit('test2(123456)', 'from __main__ import test2',
#                       number=1000000)
#    print(t2 / 100000000)
    t3 = timeit.timeit('test3(123456)', 'from __main__ import test3',
                       number=1000000)
    print(t3 / 100000000)

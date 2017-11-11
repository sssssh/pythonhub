import timeit
from math import sin


def tight_loop_slow(iterations):
    result = 0
    for i in range(iterations):
        result += sin(i)


def tight_loop_fast(iterations):
    result = 0
    local_sin = sin
    for i in range(iterations):
        result += local_sin(i)


if __name__ == '__main__':
    slow = timeit.timeit('tight_loop_slow(10000000)',
                         'from __main__ import tight_loop_slow', number=1)
    print(slow)

    fast = timeit.timeit("tight_loop_fast(10000000)",
                         "from __main__ import tight_loop_fast", number=1)
    print(fast)

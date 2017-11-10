import timeit


append_list = []
insert_list = []


def append_(haystack):
    for item in haystack:
        append_list.append(item)
        return True
    return -1


def insert_(haystack):
    for item in haystack:
        insert_list.insert(0, item)
        return True
    return -1


if __name__ == "__main__":
    setup = 'from __main__ import (haystack, append_, insert_)'
    iterations = 1000

    for haystack_size in (10 ** 5, 10 ** 6, 10 ** 7):
        haystack = range(haystack_size)
#        append_(haystack)
        t = timeit.timeit(
            stmt='append_(haystack)',
            setup=setup,
            number=iterations
        )
        print("haystack_size: {} -- function: {} -- time: {}".format(
            len(haystack), 'append_(haystack)', t / iterations))
        print(len(append_list))
        append_list = []

    for haystack_size in (10 ** 5, 10 ** 6, 10 ** 7):
        haystack = range(haystack_size)
 #       insert_(haystack)
        t = timeit.timeit(
            stmt='insert_(haystack)',
            setup=setup,
            number=iterations
        )
        print("haystack_size: {} -- function: {} -- time: {}".format(
            len(haystack), 'insert_(haystack)', t / iterations))
        print(len(insert_list))
        insert_list = []

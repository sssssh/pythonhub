from itertools import dropwhile


print(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))


def greater_than_five(x):
    return x > 5


print(dropwhile(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10]))

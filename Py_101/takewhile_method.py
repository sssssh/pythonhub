from itertools import takewhile, dropwhile

# takewhile module is basically the opposite of the dropwhile
# so once takewhile sees the False, it will ignore the rest of items in the iterable
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

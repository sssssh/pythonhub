from itertools import cycle


# cycle(iterable)
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1

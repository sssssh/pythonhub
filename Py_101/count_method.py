from itertools import count


# count(start=0, step=1)
for i in count(10):
    if i > 20:
        break
    else:
        print(i)

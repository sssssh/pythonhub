from itertools import islice, count


for i in islice(count(10), 5):
    print(i)

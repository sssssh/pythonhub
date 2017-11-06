import random
from collections import defaultdict
from collections import Counter


def some_iterator(count=10000, seed=0):
    random.seed(seed, version=1)
    for i in range(count):
        yield random.randint(-1, 36)


frequency = defaultdict(int)
for k in some_iterator():
    frequency[k] += 1


print(frequency)


by_value = defaultdict(list)
for k in frequency:
    by_value[frequency[k]].append(k)


for freq in sorted(by_value, reverse=True):
    print(by_value[freq], freq)


print("expected", 10000 // 38)


frequency = Counter(some_iterator())


print(frequency)


for k, freq in frequency.most_common():
    print(k, freq)


print("expected", 10000 // 38)

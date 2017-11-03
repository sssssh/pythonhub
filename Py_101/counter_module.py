from collections import Counter


counter = Counter('superfluous')
print(list(counter.elements()))
print(counter.most_common())


counter_one = Counter('superfluous')
counter_two = Counter('super')
print(counter_one.subtract(counter_two))
print(counter_one)

import operator
from itertools import accumulate


print(list(accumulate(range(10))))
print(list(accumulate(range(1, 5), operator.mul)))

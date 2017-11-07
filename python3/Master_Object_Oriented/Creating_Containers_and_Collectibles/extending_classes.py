import math


def mean(outcomes):
    return sum(outcomes) / len(outcomes)


def stdev(outcomes):
    n = len(outcomes)
    return math.sqrt(n * sum(x ** 2 for x in outcomes) -
                     sum(outcomes) ** 2) / n


test_case = [2, 4, 4, 4, 5, 5, 7, 9]
assert mean(test_case) == 5
assert stdev(test_case) == 2
print("Passed Unit Tests")


# lazy stats list class
class StatsList(list):
    @property
    def mean(self):
        return sum(self) / len(self)

    @property
    def stdev(self):
        n = len(self)
        return math.sqrt(n * sum(x ** 2 for x in self) -
                         sum(self) ** 2) / n


tc = StatsList([2, 4, 4, 4, 5, 5, 7, 9])
print(tc.mean, tc.stdev)


# eager stats list class
class StatsList2(list):
    def __init__(self, *args, **kw):
        self.sum0 = 0  # len(self)
        self.sum1 = 0  # sum(self)
        self.sum2 = 0  # sum(x**2 for x in self)
        super().__init__(**args, **kw)
        for x in self:
            self._new(x)

    def _new(self, value):
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value

    def _rmv(self, value):
        self.sum0 -= 1
        self.sum1 -= value
        self.sum2 -= value * value

    def insert(self, index, value):
        super().insert(index, value)
        self._new(value)

    def append(self, value):
        super().append(value)
        self._new(value)

    def extend(self, sequence):
        super().extend(sequence)
        for value in sequence:
            self._new(value)

    def pop(self, index=0):
        value = super().pop(index)
        self._rmv(value)
        return value

    def remove(self, value):
        super().remove(value)
        self._rmv(value)

    def __iadd__(self, sequence):
        result = super().__iadd__(sequence)
        for value in sequence:
            self._new(value)
        return result

    @property
    def mean(self):
        return self.sum1 / self.sum0

    @property
    def stdev(self):
        return math.sqrt(self.sum0 * self.sum2 -
                         self.sum1 * self.sum1) / self.sum0

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            olds = [self[i] for i in range(start, stop, step)]
            super().__setitem__(index, value)
            for x in olds:
                self._rmv(x)
            for x in value:
                self._new(x)
        else:
            old = self[index]
            super().__setitem__(index, value)
            self._rmv(old)
            self._new(value)

    def __delitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            olds = [self[i] for i in range(start, stop, step)]
            super().__delitem__(index)
            for x in olds:
                self._rmv(x)
            else:
                old = self[index]
                super().__delitem__(index)
                self._rmv(old)


sl2 = StatsList2([2, 4, 3, 4, 5, 5, 7, 9, 10])
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
sl2[2] = 4
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
del sl2[-1]
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
sl2.insert(0, -1)
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
r = sl2.pop()
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)

sl2.append(1)
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
sl2.extend([10, 11, 12])
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
try:
    sl2.remove(-2)
except ValueError:
    pass
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)
sl2 += [21, 22, 23]
print(sl2, sl2.sum0, sl2.sum1, sl2.sum2)

tc = StatsList([2, 4, 4, 4, 5, 5, 7, 9, 1, 10, 11, 12, 21, 22, 23])
print("expected", len(tc), "actual", sl2.sum0)
print("expected", sum(tc), "actual", sl2.sum1)
print("expected", sum(x*x for x in tc), "actual", sl2.sum2)
assert tc.mean == sl2.mean
assert tc.stdev == sl2.stdev

sl2a = StatsList2([2, 4, 3, 4, 5, 5, 7, 9, 10])
del sl2a[1:3]
print(sl2a, sl2a.sum0, sl2a.sum1, sl2a.sum2)


# stats list wrapper
class StatsList3:
    def __init__(self):
        self._list = list()
        self.sum0 = 0
        self.sum1 = 0
        self.sum2 = 0

    def append(self, value):
        self._list.append(value)
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value

    def __getitem__(self, index):
        return self._list.__getitem__(index)

    @property
    def mean(self):
        return self.sum1 / self.sum0

    @property
    def stdev(self):
        return math.sqrt(self.sum0 * self.sum2 -
                         self.sum1 * self.sum1) / self.sum0


sl3 = StatsList3()
for data in 2, 4, 4, 4, 5, 5, 7, 9:
    sl3.append(data)
print(sl3.mean, sl3.stdev)

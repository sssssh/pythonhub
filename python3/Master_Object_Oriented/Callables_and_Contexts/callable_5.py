import collections.abc


class Power5(collections.abc.Callable):
    def __init__(self):
        self.memo = {}

    def __call__(self, x, n):
        if (x, n) not in self.memo:
            if n == 0:
                self.memo[x, n] = 1
            elif n % 2 == 1:
                self.memo[x, n] = self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t = self.__call__(x, n // 2)
                self.memo[x, n] = t * t
            else:
                raise Exception("Logic Error")
        return self.memo[x, n]


pow5 = Power5()
print(pow5(2, 1024))

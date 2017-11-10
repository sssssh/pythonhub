import collections.abc


class Power4(collections.abc.Callable):
    def __call__(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1) * x
        else:
            t = self.__call__(x, n // 2)
            return t * t


pow4 = Power4()
print(pow4(2, 1024))

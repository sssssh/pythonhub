import collections.abc


class Power4i(collections.abc.Callable):
    def __call__(self, x, n):
        p = 1
        while n != 0:
            if n % 2 == 1:
                p *= x
                n -= 1
            else:
                t = self.__call__(x, n // 2)
                p *= t
                p *= t
                n = 0
        return p


pow4i = Power4i()
print(pow4i(2, 1024))

import collections.abc


class Power2(collections.abc.Callable):
    def __call_(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p


try:
    pow2 = Power2()
except TypeError as e:
    print(e)

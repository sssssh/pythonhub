import collections.abc


class Power1(collections.abc.Callable):
    def __call_(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p


pow1 = Power1()
print(pow1(2, 1024))

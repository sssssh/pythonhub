from functools import lru_cache


@lru_cache(None)
def pow6(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow6(x, n-1) * x
    else:
        t = pow6(x, n // 2)
        return t * t


print(pow6(2, 1024))

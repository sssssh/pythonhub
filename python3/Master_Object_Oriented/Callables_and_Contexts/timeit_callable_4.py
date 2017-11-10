import timeit


recursive = timeit.timeit("pow4(2,1024)","""
import collections.abc
class Power4( collections.abc.Callable ):
    def __call__( self, x, n ):
        if n == 0: return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1) * x
        else: # n % 2 == 0:
            t= self.__call__(x, n//2)
            return t*t

pow4= Power4()
""", number=100000)
print("Recursive", recursive)

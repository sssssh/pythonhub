import timeit


iterative = timeit.timeit( "pow1(2,1024)","""
import collections.abc
class Power1( collections.abc.Callable ):
    def __call__( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p

pow1= Power1()
""", number=100000)  # otherwise it takes 2 minutes
print("Iterative", iterative)

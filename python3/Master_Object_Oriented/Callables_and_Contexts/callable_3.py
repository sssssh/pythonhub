class Power3:
    def __call_(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p


pow3 = Power3()
try:
    print(pow3(2, 1024))
except TypeError as e:
    print(e)

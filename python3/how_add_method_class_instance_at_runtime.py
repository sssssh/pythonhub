import types
from itertools import chain


# python2 dict.items() 返回 list.
# python3 dict.items() 返回 dict_items([()])
# chain 返回的是可迭代对象
def __str__(self):
    classStr = ''
    for name, value in chain(self.__class__.__dict__.items(),
                             self.__dict__.items()):
        print(name, value)
        classStr += name.ljust(15) + '\t' + str(value) + '\n'
    return classStr


def addStr(anInstance):
    anInstance.__str__ = types.MethodType(__str__, anInstance)


# Test it
class TestClass:
    classSig = 'My Sig'
    def __init__(self, a=1, b=2, c=3):
        self.a = a
        self.b = b
        self.c = c


if __name__ == '__main__':
    test = TestClass()
    print(test)
    addStr(test)
    print(test)

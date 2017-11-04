# Python 2
class MyParentClass(object):
    def __init__(self):
        pass


class SubClass(MyParentClass):
    def __init__(self):
        MyParentClass.__init__(self)


class SubClass2(MyParentClass):
    def __init__(self):
        super(SubClass2, self).__init__()


# Python 3
class MyParentClass():
    def __init__(self):
        pass


class SubClass(MyParentClass):
    def __init__(self):
        super().__init__()


class MyParentClass():
    def __init__(self, x, y):
        pass


class SubClass(MyParentClass):
    def __init__(self, x, y):
        super().__init__(x, y)


# method resolution order
class X:
    def __init__(self):
        print('X')
        super().__init__()


class Y:
    def __init__(self):
        print('Y')
        super().__init__()


class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)


class Base:
    var = 5

    def __init__(self):
        pass


class X(Base):
    def __init__(self):
        print('X')
        super().__init__()


class Y(Base):
    var = 10

    def __init__(self):
        print('Y')
        super().__init__()


class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)
print(super(Z, z).var)


class Base():
    def __init__(self):
        s = super()
        print(s.__thisclass__)
        print(s.__self_class__)
        s.__init__()


class SubClass(Base):
    pass


sub = SubClass()

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

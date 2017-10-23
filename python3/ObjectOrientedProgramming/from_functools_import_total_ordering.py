# Given a class defining one or more rich comparison ordering methods, this class decorator supplies the rest
# The class must define one of __lt__(), __le__(), __gt__(), or __ge__().
# In addition, the class should supply an __eq__() method.
from functools import total_ordering
from abc import ABCMeta, abstractmethod
from math import pi


@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


# 1
class Rectangle(object):
    def __init__(self, weight, height):
        self.w = weight
        self.h = height

    def area(self):
        return self.w * self.h

    def __lt__(self, rect):
        if self.area() < rect.area():
            return True
        else:
            return False

    def __le__(self, rect):
        if self.area() <= rect.area():
            return True
        else:
            return False

    def __gt__(self, rect):
        if self.area() > rect.area():
            return True
        else:
            return False

    def __eq__(self, rect):
        if self.area() == rect.area():
            return True
        else:
            return False

    def __ne__(self, rect):
        if self.area() != rect.area():
            return True
        else:
            return False


rect1 = Rectangle(1.0, 2.0)
rect2 = Rectangle(1.0, 1.0)
print(rect1 < rect2)


# 2
@total_ordering
class Rectangle2(object):
    def __init__(self, weight, height):
        self.w = weight
        self.h = height

    def area(self):
        return self.w * self.h

    def __lt__(self, rect):
        return self.area() < rect.area()

    def __eq__(self, rect):
        return self.area() == rect.area()


# 3
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, object):
        if not isinstance(object, Shape):
            return TypeError('object is not Shape')
        return self.area() < object.area()

    def __eq__(self, object):
        if not isinstance(object, Shape):
            return TypeError('object is not Shape')
        return self.area() == object.area()


class Rentangle2(Shape):
    def __init__(self, weight, height):
        self.w = weight
        self.h = height

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi


r1 = Rentangle2(3, 2)
c1 = Circle(3)
print(r1 > c1)

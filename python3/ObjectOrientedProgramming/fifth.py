import math
import sys
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlopen


# distances - no objects
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)


def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter


# distances by objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)


class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


# object - polygon init
class Polygon2:
    def __init__(self, points=[]):
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


# python ugly as java
class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


# python pretty as python
class Color2:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


c = Color2("#ff0000", "bright red")
print(c.name)
c.name = "red"


# setting name in method
class Color3:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def get_name(self):
        return self._name


# setting name property
class Color4:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


# property arguments
class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly,
                     "This is a silly property")


# property decorator get
class Foo:
    @property
    def foo(self):
        return "bar"


# property decorator arguments
class Silly2:
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly


# property decorator get set
class Foo2:
    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value


foo = Foo2()
foo.foo = 2
print(foo.foo)


# read only setattr
class ReadOnlyX:
    def __setattr__(self, attr, value):
        if attr == "x":
            raise AttributeError("X is immutable")
        super().__setattr__(attr, value)


# read only getattribute
class ReadOnlyY:
    def __getattribute__(self, attr):
        if attr == "y":
            return "Just Try and Change Me!"
        return super().__getattribute__(attr)


read_x = ReadOnlyX()
# read_x.x = 1
# print(read_x.x)
read_x.a = 1

read_y = ReadOnlyY()
# read_y.y = 2
read_y.a = 2


# cache getter

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


# average property
class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)


_list = AverageList([1, 2, 3, 4, 5])
print(_list.average)


# zipsearch
class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(
            filename))

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


# ZipReplace(*sys.argv[1:4]).zip_find_replace()

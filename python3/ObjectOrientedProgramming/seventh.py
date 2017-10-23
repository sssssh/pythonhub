import string
import random
from operator import itemgetter
from collections import Iterable


# reversible objects
normal_list = [1, 2, 3, 4, 5]


class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBackwards():
    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print('----', seq)
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")


# enumerate line numbers
def enumerate_line(filename):
    with open(filename) as files:
        for index, line in enumerate(files):
            print("{0}: {1}".format(index+1, line), end='')


# zip to enumerate
def zip_enumerate(container):
    return zip(range(len(container)), container)


# enumerate max min
def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=itemgetter(1))
    maximum = max(enumerate(seq), key=itemgetter(1))
    return minimum[0], maximum[0]


# file
class HandlerFile:
    def __init__(self, filename):
        self.filename = filename

    def readfile(self):
        files = open(self.filename).read()
        files.close()
        return files

    def writefile(self, contents):
        files = open(self.filename, 'w')
        files.write(contents)
        files.close

    def withfiles(self):
        with open(self.filename) as files:
            for line in files:
                print(line, end='')

    def getdata(self):
        with open(self.filename) as file:
            header = file.readline().strip().split('\t')
            contacts = [
                dict(zip(header, line.strip().split('\t'))) for line in file]
        return contacts


# context manager
class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, types, value, tb):
        self.result = "".join(self)


with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

print(joiner.result)


'''
# bad kw default
number = 5
def funky_function(number=number):
    print(number)

number=6
funky_function(8)
funky_function()
print(number)
'''


# link downloader
def get_pages(links):
    if not isinstance(links, Iterable) or isinstance(
            links, (bytes, str)):
        links = [links]
    for link in links:
        # download the link with urllib
        print(link)


# link downloader var arg
def get_pages2(*links):
    for link in links:
        # download the link with urllib
        print(link)

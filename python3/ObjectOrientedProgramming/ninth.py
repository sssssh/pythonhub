import csv
import re
from collections import namedtuple


# iterator
class CapitalIterable:
    def __init__(self, _string):
        self._string = _string

    def __iter__(self):
        return CapitalIterator(self._string)


class CapitalIterator:
    def __init__(self, _string):
        self.words = [w.capitalize() for w in _string.split()]
        self._index = 0

    def __next__(self):
        if self._index == len(self.words):
            raise StopIteration()

        word = self.words[self._index]
        self._index += 1
        return word

    def __iter__(self):
        return self


# for loop converter
input_strings = ['1', '5', '28', '131', '3']
output_integers = []
for num in input_strings:
    output_integers.append(int(num))


# listcomp converter
listcomp_integers = [int(num) for num in input_strings]


# listcomp exclude
exclude_integers = [int(num) for num in input_strings if len(num) < 3]


# set comprehension
Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]
fantasy_authors = {
        b.author for b in books if b.genre == 'fantasy'}


# dict comprehension
fantasy_titles = {
    b.title: b for b in books if b.genre == 'fantasy'}


# log processor
existfilename = ''
newfilename = ''


with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        warnings = (l for l in infile if "WARNING" in l)
        for l in warnings:
            outfile.write(l)


# delete warning
with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        warnings = (l.replace('\tWARNING', '')
                    for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)


# delete warning
with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        for l in infile:
            if 'WARNING' in l:
                outfile.write(l.replace('\tWARNING', ''))


# delete warnings
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and 'WARNING' not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace('\WARNING', '')


with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)


# delete warnings
def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("\tWARNING", '')


with open(existfilename) as infile:
    with open(newfilename, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)


# delete warning
def warning_filter(infilename):
    with open(infilename) as infiles:
        yield from (
             l.replace('\tWARNING', '')
             for l in infiles
             if 'WARNING' in l
        )


filter = warning_filter(existfilename)
with open(existfilename, 'w') as outfile:
    for l in filter:
        outfile.write(l)


# yield from filesystem
class File:
    def __init__(self, name):
        self.name = name


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.children = []


root = Folder('')
etc = Folder('etc')
root.children.append(etc)
etc.children.append(File('passwd'))
etc.children.append(File('groups'))
httpd = Folder('httpd')
etc.children.append(httpd)
httpd.children.append(File('http.conf'))
var = Folder('var')
root.children.append(var)
log = Folder('log')
var.children.append(log)
log.children.append(File('messages'))
log.children.append(File('kernel'))


def walk(_file):
    if isinstance(_file, Folder):
        yield _file.name + '/'
        for f in _file.children:
            yield from walk(f)
    else:
        yield _file.name


for filename in walk(root):
    print(filename)


# basic count coroutine
def tally():
    score = 0
    while True:
        increment = yield score
        score += 1


# kernel log
def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]


def get_serials(filename):
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        bus = matcher.send('(sd \S+) {}.*'.format(re.escape(device)))
        serial = matcher.send('{} \(SERIAL=([^)]*)\)'.format(bus))
        yield serial
        device = matcher.send(ERROR_RE)


for serial_number in get_serials('EXAMPLE_LOG.log'):
    print(serial_number)


# load dataset
dataset_filename = 'colors.csv'


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]

for color, name in load_colors(dataset_filename):
    print("RGB {} is named {}".format(color, name))

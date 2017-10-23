import time
import datetime
import shutil
import os.path
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


# kwarg options
class Options:
    default_options = {
        "port": 21,
        "host": 'localhost',
        "username": None,
        "password": None,
        "debug": False,
        }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]


# all arguments
def augmented_move(target_folder, *filenames,
                   verbose=False, **specific):
    '''Move all filenames into the target_folder, allowing
    specific treatment of certain files.'''

    def print_verbose(message, filename):
        '''print the message only if verbose is enabled'''
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == 'copy':
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)


# unpacking arguments
def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)


# function objects
def my_function():
    print("The Function Was Called")


my_function.description = "A silly function"


def second_function():
    print("The second was called")


second_function.description = "A sillier function."


def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()


another_function(my_function)
another_function(second_function)


# timer
class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + \
                   datetime.timedelta(seconds=delay)

        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


# timer test
def format_time(message, *args):
    now = datetime.datetime.strftime("%I:%M:%S")
    print(message.format(*args, now=now))


def one(timer):
    format_time("{now}: Called One")


def two(timer):
    format_time("{now}: Called Two")


def three(timer):
    format_time("{now}: Called Three")


class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self.repeater)


timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater)
format_time("{now}: Starting")
timer.run()


# add function to object
class A:
    def print(self):
        print("my class is A")


def fake_print():
    print("my class is not A")


a = A()
a.print()
a.print = fake_print
a.print()


# callable repeat
class Repeater2:
    def __init__(self):
        self.count = 0

    def __call__(self, timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self)


timer = Timer()
timer.call_after(5, Repeater())
format_time("{now}: Starting")
timer.run()

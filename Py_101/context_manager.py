import sys
from io import StringIO
from contextlib import contextmanager, closing, suppress
from connectlib import redirect_stdout, ExitStack
from urllib.request import urlopen


# create a context manager
@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print("Closing file")
        f_obj.close()


'''
# contextlib.closing(thing)
@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()
'''


# contextlib.suppress(*exceptions)
'''
with open('fauxfile.txt') as fobj:
    for line in fobj:
        print(line)
'''
with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)


# contextlib.redirect_stdout / redirect_stderr
path = '/Users/noodle/Desktop/text.txt'
with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)


with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)


# ExitStack
with ExitStack as stack:
    file_objects = [stack.enter_context(open(filename))
                    for filename in filenames]


# reentrant context manager
@contextmanager
def single():
    print('Yielding')
    yield
    print('Exiting context manager')


context = single()
with context:
    pass
with context:
    pass


if __name__ == '__main__':
    with file_open("/Users/noodle/Desktop/test.txt") as f_obj:
        f_obj.write("Testing context managers")

    with closing(urlopen('http://www.google.com')) as webpage:
        for line in webpage:
            pass

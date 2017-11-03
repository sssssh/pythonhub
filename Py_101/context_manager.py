from contextlib import contextmanager, closing
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


if __name__ == '__main__':
    with file_open("/Users/noodle/Desktop/test.txt") as f_obj:
        f_obj.write("Testing context managers")

    with closing(urlopen('http://www.google.com')) as webpage:
        for line in webpage:
            pass

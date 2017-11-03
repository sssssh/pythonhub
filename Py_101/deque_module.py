import string
from collections import deque


d = deque(string.ascii_lowercase)
d.append('bork')
d.appendleft('test')
d.rotate(1)


def get_last(filename, n=5):
    """
    Return the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise


# if the file is very very big? how did i do?

# regular import
import sys
import os, sys, time
import sys as system
import urllib.error
# Using from
from functools import lru_cache
from os import *
from os import path, walk, unlink
from os import uname, remove
from os import (path, walk, unlink, uname,
                remove, rename)
from os import path, walk, unlink, uname, \
    remove, rename

# relative imports
'''
my_package/
    __init__.py
    subpackage1/
        __init__.py
        module_x.py
        module_y.py
    subpackage2/
        __init__.py
        module_z.py
    module_a.py
'''
from . import subpackage1
from . import subpackage2

from . import module_x
from . import module_y

from .module_y import spam as ham

sys.path.append('/path/to/folder/containing/my_package')
import my_package

# optional imports
try:
    # for python3
    from http.client import responses
except ImportError:  # for python 2.5-2.7
    try:
        from httplib import responses  # NOQA
    except ImportError:  # for python 2.4
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
        responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])

try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    # python3
    from urllib.parse import urljoin
    from urllib.request import urlopen


# local imports
def square_root(a):
    import math
    return math.sqrt


def my_pow(base_num, power):
    return math.pow(base_num, power)

# import pitfalls

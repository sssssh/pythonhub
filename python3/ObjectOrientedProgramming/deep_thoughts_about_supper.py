__author__ = 'Raymond Hettinger'
__article__ = """
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
https://www.blog.pythonlibrary.org/2014/01/21/python-201-what-is-super/
"""
import logging.info


# a subclass for extending a method from one of the builtin classes
class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info("Settingto %r" % (key, value))
        super().__setitem__(key, value)

import atexit
import sys
import logging
import logging.config
import yaml
from collections import Counter


config3 = """
version: 1
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  audit_file:
    class: logging.FileHandler
    filename: p3_c14_audit.log
    encoding: utf-8
    formatter: basic
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  verbose:
    handlers: [console]
    level: INFO
    propagate: False # Added
  audit:
    handlers: [console,audit_file]
    level: INFO
    propagate: False # Added
root: # Added
  handlers: [console]
  level: INFO
"""


class Main:
    def __init__(self):
        self.balance = Counter()
        self.log = logging.getLogger(self.__class__.__qualname__)

    def run(self):
        self.log.info("Start")

        self.balance['count'] += 1
        self.balance['balance'] += 3.14

        self.log.info("Counts {0}".format(self.balance))

        for k in self.balance:
            self.loginfo("{0:.<16s} {1:n}".format(
                k, self.balance[k]))


def demo_a():
    logging.config.dictConfig(yaml.load(config3))
    try:
        application = Main()
        status = application.run()
    except Exception as e:
        logging.exception(e)
        status = 2
    finally:
        logging.shutdown()

    # sys.exit(status)


def demo_b():
    logging.config.dictConfig(yaml.load(config3))
    atexit.register(logging.shutdown)

    try:
        application = Main()
        status = application.run()
    except Exception as e:
        logging.exception(e)
        status = 2

    # sys.exit(status)

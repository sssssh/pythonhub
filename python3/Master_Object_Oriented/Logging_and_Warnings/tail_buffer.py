import logging
import logging.config
import logging.handlers
import yaml


class TailHandler(logging.handlers.MemoryHandler):

    def shouldFlush(self, record):
        '''
        Check for buffer full or a record at the flushLevel or higher.
        '''
        if record.levelno >= self.flushLevel:
            return True
        while len(self.buffer) >= self.capacity:
            self.acquire()
            try:
                del self.buffer[0]
            finally:
                self.release()


config8 = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  tail:
    (): __main__.TailHandler
    target: cfg://handlers.console
    capacity: 5
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  test:
    handlers: [tail]
    level: DEBUG
    propagate: False
root:
  handlers: [console]
  level: INFO
"""


def demo():

    logging.config.dictConfig(yaml.load(config8))
    log = logging.getLogger("test.demo8")

    print("Last 5 before error")

    for i in range(20):
        log.debug("Message {:d}".format(i))

    log.error("Eoor causes dump of last 5")

    print("Last 5 before shutdown")

    for i in range(20, 40):
        log.debug("Message {:d}".format(i))

    logging.shutdown()

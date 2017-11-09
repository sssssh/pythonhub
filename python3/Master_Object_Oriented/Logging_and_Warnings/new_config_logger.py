import yaml
import atexit
import logging
from simple_logging import logged


config5 = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  audit_file:
    class: logging.FileHandler
    filename: p3_c14_audit.log
    encoding: utf-8
    formatter: detailed
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  detailed:
    style: "{"
    format: "{levelname:s}:{name:s}:{asctime:s}:{message:s}"
    datefmt: "%Y-%m-%d %H:%M:%S"
loggers:
  audit:
    handlers: [console,audit_file]
    level: INFO
    propagate: False
root:
  handlers: [console]
  level: INFO
"""


def demo():

    @logged
    class BettingStrategy:
        def bet(self):
            raise NotImplementedError("No bet method")

        def record_win(self):
            pass

        def record_loss(self):
            pass

    @logged
    class OneThreeTwoSix(BettingStrategy):
        def __init__(self):
            self.wins = 0

        def _state(self):
            return dict(wins=self.wins)

        def bet(self):
            bet = {0: 1, 1: 3, 2: 2, 3: 6}[self.wins % 4]
            self.logger.debug("Bet {1}; based on {0}".format(self._state(), bet))

        def record_win(self):
            self.wins += 1
            self.logger.debug("Win: {0}".format(self._state()))

        def record_loss(self):
            self.wins = 0
            self.logger.debug("Loss: {0}".format(self._state()))

    def audited(class_):
        class_.logger = logging.getLogger(class_.__qualname__)
        class_.audit = logging.getLogger("audit." + class_.__qualname__)
        return class_

    @audited
    class Table:
        def bet(self, bet, amount):
            self.audit.info("Bet {0} Amount {1}".format(bet, amount))

    logging.config.dictConfig(yaml.load(config5))
    atexit.register(logging.shutdown)
    log = logging.getLogger("main")
    log.info("Starting")
    application = Table()
    application.bet("One", 1)
    application.bet("Two", 2)
    log.info("Finish")
    logging.shutdown()

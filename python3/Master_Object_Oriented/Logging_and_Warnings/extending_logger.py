import threading
import yaml
import logging
from collections import Callable


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

    class UserLogRecord(Callable):
        def __init__(self):
            self.previous = logging.getLogRecordFactory()

        def __call__(self, *args, **kwargs):
            print("Building log with", args, kwargs, getattr(self, 'extra', {}))
            user = kwargs.pop('user', None)
            record = self.previous(*args, **kwargs)
            record.user = user
            return record

    class UserLogAdapter(logging.LoggerAdapter):
        def process(self, msg, kwargs):
            kwargs['user'] = self.extra.get('user', None)
            return msg, kwargs

    logging.config.dictConfig(yaml.load(config5))
    logging.setLogRecordFactory(UserLogRecord())

    log = logging.getLogger("test.demo6")
    for h in logging.getLogger().handlers:
        h.setFormatter(logging.Formatter(fmt="{user}:{name}:{levelname}:{message}",
                                         style="{"))

    data = threading.local()
    data.user = "Some User"
    data.ip_address = '127.0.0.1'

    log.info('message without user')


    # auth_log = logging.LoggerAdapter(log, data.__dict__)
    # auth_log = UserLogAdapter(log, data.__dict__)
    # auth_log.info("message with User")

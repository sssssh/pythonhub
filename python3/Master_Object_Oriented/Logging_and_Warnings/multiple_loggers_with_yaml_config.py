import yaml
import logging.config


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


def demo():
    config_dict = yaml.load(config3)
    print(config_dict)
    logging.config.dictConfig(config_dict)

    # logging
    verbose = logging.getLogger("verbose.example.SomeClass")
    audit = logging.getLogger("audit.example.SomeClass")
    verbose.info("Verbose information")
    audit.info("Audit record with before and after")

    print("Root Handlers:", logging.getLogger().handlers)
    print("Verbose Handlers:", logging.getLogger('verbose').handlers)
    print("Audit Handlers:", logging.getLogger('audit').handlers)

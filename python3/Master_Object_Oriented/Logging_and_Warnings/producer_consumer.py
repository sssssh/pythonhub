import yaml
import logging
import collections
import multiprocessing


consumer_config = """\
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  combined:
    handlers: [ console ]
    formatter: detail
    level: INFO
    propagate: False
root:
  handlers: [ console ]
  level: INFO
"""


class Log_Consumer_1(multiprocessing.Process):
    """In effect, an instance of QueueListener."""
    def __init__(self, queue):
        super().__init__()
        logging.config.dictConfig(yaml.load(consumer_config))
        self.combined = logging.getLogger("combined." + self.__class__.__qualname__)
        self.log = logging.getLogger(self.__class__.__qualname__)
        self.counts = collections.Counter()

    def run(self):
        self.log.info("Consumer Started")
        while True:
            log_record = self.source.get()
            if log_record == None:
                break
            self.combined.handle(log_record)
            words = log_record.getMessage().split()
            self.counts[words[0], words[1]] += 1
        self.log.info("Consumer Finished")
        self.log.info(self.counts)


class Log_Producer(multiprocessing.Process):
    handler_class = logging.handlers.QueueHandler

    def __init__(self, proc_id, queue):
        self.proc_id = proc_id
        self.destination = queue
        super().__init__()
        self.log = logging.getLogger(
            "{0}.{1}".format(self.__class__.__qualname__, self.proc_id))
        self.log.handlers = [self.handler_class(self.destination)]
        self.log.setLevel(logging.INFO)

    def run(self):
        self.log.info("Producer {0} Started".format(self.proc_id))
        for i in range(100):
            self.log.info("Producer {:d} Message {:d}".format(self.proc_id, i))
        self.log.info("Producer {0} Finished".format(self.proc_id))


def demo():
    queue1 = multiprocessing.Queue(100)

    consumer = Log_Consumer_1(queue1)
    consumer.start()

    producers = []
    for i in range(10):
        proc = Log_Producer(i, queue1)
        proc.start()
        producers.append(proc)

    for p in producers:
        p.join()

    queue1.put(None)
    consumer.join()
    logging.shutdown()

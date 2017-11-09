import multiprocessing
import logging
from producer_consumer import Log_Producer, Log_Consumer_1


class WaitQueueHandler(logging.handlers.QueueHandler):
    def enqueue(self, record):
        self.queue.put(record)


class Log_Producer_2(Log_Producer):
    handler_class = WaitQueueHandler


queue2 = multiprocessing.Queue(100)


consumer2 = Log_Consumer_1(queue2)
consumer2.start()


producers = []
for i in range(10):
    proc = Log_Producer_2(i, queue2)
    proc.start()
    producers.append(proc)


for p in producers:
    p.join()

queue2.put(None)

consumer2.join()

logging.shutdown()

import logging
from multiprocessing import Process, Lock, log_to_stderr, get_logger


def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()

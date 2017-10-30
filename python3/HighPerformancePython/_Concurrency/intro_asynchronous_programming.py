from queue import Queue
from functools import partial


eventloop = None


class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()


def do_hello():
    global eventloop
    print("Hello")
    eventloop.put(do_world)


def do_world():
    global eventloop
    print("world")
    eventloop.put(do_hello)


# 事件循环编程能采取两种方式：回调或者future
def save_value(value, callback):
    print("Saving {} to database".format(value))
    save_result_to_db(value, callback)


def print_response(db_response):
    print("Response from database: {}".format(db_response))


def save_result_to_db(result, callback):
    pass


# futures
@coroutine
def save_value(value, callback):
    print("Saving {} to database".format(value))
    db_response = yield save_result_to_db(value, callback)
    print("Response from database: {}".format(db_response))


if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(do_hello)
    eventloop.start()

    # callback
    eventloop.put(
        partial(save_value, "Hello World", print_response)

    # futures
    eventloop.put(
        partial(save_value, "Hello World")

# 事件循环 和 异步
# 函数之间的切换会有开销。内核必须花费时间来设置在内存中被调用的函数，缓存的状态将变得不可预测。
# 程序有许多I/O等待时，并发给出了最好的结果。
# 尽管这种切换的确有它的开销，但它要比把I/O等待时间利用起来从而取得的收益要小得多。

# 大小都是相对而言的（参考参照物）

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


if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(do_hello)
    eventloop.start()


# 事件循环 和 异步
# 函数之间的切换会有开销。内核必须花费时间来设置在内存中被调用的函数，缓存的状态将变得不可预测。
# 程序有许多I/O等待时，并发给出了最好的结果。
# 尽管这种切换的确有它的开销，但它要比把I/O等待时间利用起来从而取得的收益要小得多。

# 大小都是相对而言的（参考参照物）

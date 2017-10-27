import time
import socket
import gzip
from io import BytesIO


# simple socket
def respond(client):
    res = input("Enter a value: ")
    client.send(bytes(res, 'utf-8'))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(client)
finally:
    server.close()


# simple client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2401))
print("Received: {}".format(client.recv(1024)))
client.close()


# logging decorator
class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print("Sending {0} to {1}".format(
            data, self.socket.getpeername()[0]))
        self.socket.send(data)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()


# gzip decorator
class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(GzipSocket(client))
finally:
    server.close()


# logging decorator
def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(
            func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(
            func.__name__, time.time() - now))
        return return_value
    return wrapper


def test1(a, b, c):
    print("\ttest1 called")


def test2(a, b):
    print("\ttest2 called")


def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)


# decorator syntax
@log_calls
def test4(a, b, c):
    print("\ttest4 called")


# observer core
class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observer.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._updata_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._updata_observers()

    def _updata_observers(self):
        for observer in self.observers:
            observer()

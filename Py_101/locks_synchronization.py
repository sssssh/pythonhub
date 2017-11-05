import threading


total = 0
lock = threading.Lock()


print('------------', total)


def update_total(amount):
    global total
    total += amount
    print(total)


def update_total2(amount):
    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()  # ensure htat the lock is always released
#    except:
#        pass
    print(total)


def update_total3(amount):
    global total
    with lock:
        total += amount
    print(total)


if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()
    print('------------', total)

    for i in range(10):
        my_thread2 = threading.Thread(
            target=update_total2, args=(6,))
        my_thread2.start()

    print('------------', total)

    for i in range(10):
        my_thread3 = threading.Thread(
            target=update_total3, args=(7,))
        my_thread3.start()

    print('-----------', total)

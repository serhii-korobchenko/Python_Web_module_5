from multiprocessing import Process, Value
from time import sleep
import sys


def useless(name, delay, val):
    print(f'{name} Started')
    sleep(delay)
    val.value += 1
    print(f'{name} Done')
    sys.exit(0)


if __name__ == '__main__':
    v = Value('d', 0)
    p1 = Process(target=useless, args=('first', 2, v))
    p2 = Process(target=useless, args=('second', 3, v))

    p1.start()
    p2.start()

    print(p1.exitcode, p2.exitcode)  # None, None

    p1.join()
    p2.join()

    print(p1.exitcode, p2.exitcode)  # 0, 0
    print(v.value)  # 2.0
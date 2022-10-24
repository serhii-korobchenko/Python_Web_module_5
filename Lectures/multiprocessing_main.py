from multiprocessing import Process
from time import sleep
import sys


def useless(name, delay):
    print(f'{name} Started')
    sleep(delay)
    print(f'{name} Done')
    sys.exit(0)


if __name__ == '__main__':
    p1 = Process(target=useless, args=('first', 2))
    p2 = Process(target=useless, args=('second', 2))

    p1.start()
    p2.start()

    print(p1.exitcode, p2.exitcode)  # None, None

    p1.join()
    p2.join()

    print(p1.exitcode, p2.exitcode)  # 0, 0
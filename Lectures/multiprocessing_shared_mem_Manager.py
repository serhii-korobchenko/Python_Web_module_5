from multiprocessing import Process, Manager
from time import sleep
import sys


def useless(name, delay, val):
    print(f'{name} Started')
    sleep(delay)
    val[name] = 1
    print(f'{name} Done')
    sys.exit(0)


if __name__ == '__main__':
    manager = Manager()
    m = manager.dict()
    p1 = Process(target=useless, args=('first', 2, m))
    p2 = Process(target=useless, args=('second', 2, m))

    p1.start()
    p2.start()
    print('All started')
    print(p1.exitcode, p2.exitcode)
    p1.join()
    p2.join()
    print(p1.exitcode, p2.exitcode)
    print(m)
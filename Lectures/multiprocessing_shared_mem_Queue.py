from multiprocessing import Queue, Process
from time import sleep
import sys


q = Queue()


def slave(e, name):
    print(f'{name} started...')
    val = e.get()
    print(f'{name} {val**2}')
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(target=slave, args=(q, 'first'))
    w2 = Process(target=slave, args=(q, 'second'))

    w1.start()
    w2.start()

    q.put(8)
    sleep(1)
    q.put(16)
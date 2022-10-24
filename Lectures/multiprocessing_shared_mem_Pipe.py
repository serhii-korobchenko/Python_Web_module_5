from multiprocessing import Pipe, Process
from time import sleep
import sys

rx1, tx1 = Pipe()
rx2, tx2 = Pipe()


def slave(e, name):
    print(f'{name} started...')
    val = e.recv()
    print(name, val**2)
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(target=slave, args=(rx2, 'first'))
    w2 = Process(target=slave, args=(rx1, 'second'))

    w1.start()
    w2.start()

    tx1.send(8)
    sleep(3)
    tx2.send(16)
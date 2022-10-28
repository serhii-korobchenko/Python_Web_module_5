from multiprocessing import Pool, cpu_count
import os
from time import time


def f(x):
    print(f"pid={os.getpid()}, x={x}")
    return x*x


if __name__ == '__main__':
    print (cpu_count())
    timer = time()
    with Pool(processes=2) as pool:
        print(pool.map(f, range(10)))

    print (time() - timer)
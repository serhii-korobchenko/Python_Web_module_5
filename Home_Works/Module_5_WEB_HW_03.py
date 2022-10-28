from time import time
from multiprocessing import Pool
import os




# CONCURENT VERSION

def factorize_proc(single_num):
    work_inner_list = []
    for i in range(1, single_num + 1):
        if single_num % i == 0:
            work_inner_list.append(i)

    print(f"pid={os.getpid()}, work_inner_list={work_inner_list}")
    return work_inner_list


if __name__ == '__main__':

    # MAIN BODY

    # Option 2
    print('Option 2')
    timer = time()

    with Pool(processes=2) as pool:
        input = (128, 255, 99999, 10651060)
        work_outer_list = []
        for item in pool.map(factorize_proc, input):
            work_outer_list.append(item)

    print(work_outer_list)
    print(f'Total time: {time() - timer}')

    a, b, c, d = work_outer_list
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    print('Assert: Done!')


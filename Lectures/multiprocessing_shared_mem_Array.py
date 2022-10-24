from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2


if __name__ == '__main__':
    lock = Lock()

    n = Value('i', 7)
    x = Value(c_double, 1.0 / 3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1, -6), (-5, 2), (2, 9)], lock=lock)

    p1 = Process(target=modify, args=(n, x, s, A))
    p2 = Process(target=modify, args=(n, x, s, A))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(n.value)  # 49
    print(x.value)  # 0.1111111111111111
    print(s.value)  # b'HELLO WORLD'
    print([(a.x, a.y) for a in A])  # [(1.0, 36.0), (25.0, 4.0), (4.0, 81.0)]
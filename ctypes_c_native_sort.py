
from ctypes import *
import time
import random
""" standard C library’s qsort() """

if __name__ == '__main__':
    libc = CDLL("libc.so.6")  # On Linux
    # libc = ctypes.CDLL("libc.dylib")  # On Mac
    # libc = ctypes.CDLL("msvcrt.dll")  # On Windows

    qsort = libc.qsort
    qsort.restype = None

    @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
    def py_cmp_func(a, b):
        # print("py_cmp_func", a[0], b[0])
        return a[0] - b[0]

    # Sample data for our call:
    k = 10
    x = random.sample(range(0, k), k)

    # convert list to ctypes int array
    y = (c_int * len(x))(*x)

    start_time = time.time_ns()
    qsort(y, len(y), sizeof(c_int), py_cmp_func)  
    end_time = time.time_ns()

    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print("--- %s ns ---" % (end_time - start_time))

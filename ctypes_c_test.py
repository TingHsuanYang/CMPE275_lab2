import pathlib
import sys
import ctypes
import time
import random
""" Simple examples of calling C functions through ctypes module. """

if __name__ == '__main__':
    libname = pathlib.Path().absolute()
    print("libname: ", libname)

    # Load the shared library into c types.
    if sys.platform.startswith("win"):
        c_lib = ctypes.CDLL(libname / "csort.dll")
    else:
        c_lib = ctypes.CDLL(libname / "libcsort.so")

    # Sample data for our call:
    k = 10
    x = random.sample(range(0, k), k)

    # convert list to ctypes int array
    y = (ctypes.c_int * len(x))(*x)

    start_time = time.time_ns()
    answer = c_lib.c_sort(y, len(y))
    end_time = time.time_ns()

    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print("--- %s ns ---" % (end_time - start_time))

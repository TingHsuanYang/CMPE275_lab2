import pathlib
import random
import sys
import ctypes
import time
""" Simple examples of calling C functions through ctypes module. """

if __name__ == '__main__':
    libname = pathlib.Path().absolute()
    print("libname: ", libname)

    # Load the shared library into c types.
    if sys.platform.startswith("win"):
        cpp_lib = ctypes.CDLL(libname / "cppsort.dll")
    else:
        cpp_lib = ctypes.CDLL(libname / "libcppsort.so")

    # Sample data for our call:
    k = 10
    x = random.sample(range(0, k), k)

    # convert list to ctypes int array
    y = (ctypes.c_int * len(x))(*x)

    # This produces a bad answer:
    start_time = time.time_ns()
    answer = cpp_lib.cpp_sort(y, len(y))
    end_time = time.time_ns()

    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print("--- %s ns ---" % (end_time - start_time))

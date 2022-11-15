import pathlib
import random
import sys
import ctypes
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
    answer = cpp_lib.cpp_sort(y, len(y))
    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print()

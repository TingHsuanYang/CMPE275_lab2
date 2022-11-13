import pathlib
import sys
import ctypes
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
    x = [2, 1, 4, 3, 5]
    # convert list to ctypes int array
    y = (ctypes.c_int * len(x))(*x) 
    # This produces a bad answer:
    answer = c_lib.c_sort(y, len(y))
    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print()

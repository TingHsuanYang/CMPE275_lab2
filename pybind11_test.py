import time
import random
import pybind11_cppsort

if __name__ == "__main__":
    # Sample data for our call:
    k = 1000
    x = random.sample(range(0, k), k)

    start_time = time.time_ns()
    y = pybind11_cppsort.pybind11_cpp_sort(x)

    # can't use this function, because the cpp file only accepts raw arrays.
    # you need to use py::buffer when binding the function.
    # y = pybind11_cppsort.cpp_sort(x, len(x))
    print(f"    In Python: array: {x} return sorted array {y}")
    print("--- %s ns ---" % (time.time_ns() - start_time))

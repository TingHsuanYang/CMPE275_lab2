#!/usr/bin/env python
import pybind11_cppsort
import numpy as np


if __name__ == "__main__":
    # Sample data for our call:
    x = [2, 1, 4, 3, 5]
    y = list(x)
    a = np.array([2, 1, 4, 3, 5,4])
    pybind11_cppsort.cpp_sort(a, len(a))
    print(f"    In Python: array: {x} return sorted array {a}")
    print()

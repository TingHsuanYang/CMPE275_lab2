#!/usr/bin/env python
import pybind11_cppsort

if __name__ == "__main__":
    # Sample data for our call:
    x = [2, 1, 4, 3, 5]

    y = pybind11_cppsort.pybind11_cpp_sort(x)
    print(f"    In Python: array: {x} return sorted array {y}")
    print()

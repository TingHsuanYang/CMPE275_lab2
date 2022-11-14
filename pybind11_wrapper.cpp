#include <pybind11/pybind11.h>
#include "cppsort.hpp"

PYBIND11_MODULE(pybind11_cppsort, m) {
    m.doc() = "pybind11 sort plugin"; // Optional module docstring
    m.def("cpp_sort", &cpp_sort, "A function that sorts an array");
}

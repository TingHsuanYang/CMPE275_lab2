#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "cppsort.hpp"

// swap
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// partition
int partition(std::vector<int>& array, int low, int high) {
    int pivot = array[high];
    int i = (low - 1);
    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
            i++;
            swap(&array[i], &array[j]);
        }
    }
    swap(&array[i + 1], &array[high]);
    return (i + 1);
}

// quickSort
void quickSort(std::vector<int>& array, int low, int high) {
    if (low < high) {
        int pi = partition(array, low, high);
        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}

// return a sorted vector
std::vector<int> pybind11_cpp_sort(std::vector<int> arr) {
    quickSort(arr, 0, arr.size() - 1);
    return arr;
}

PYBIND11_MODULE(pybind11_cppsort, m) {
    m.doc() = "pybind11 sort plugin";  // Optional module docstring
    m.def("pybind11_cpp_sort", &pybind11_cpp_sort, "A function that sorts an array");
}

PYBIND11_MODULE(cpp_sort, m) {
    m.doc() = "cpp_sort plugin";  // Optional module docstring
    m.def("cpp_sort", &cpp_sort, "cpp sort");
}

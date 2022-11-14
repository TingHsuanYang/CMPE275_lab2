from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("int *sort(int data[], int len);")
ffibuilder.set_source("pysort",'#include "csort_cffi.h"',sources=["csort_cffi.c"])
ffibuilder.compile()

from pysort.lib import sort
from pysort import ffi
from cffi import FFI
import numpy as np
import ctypes
import time
import random

# ff1 = FFI()
# lib = ff1.dlopen()

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(0, n))

# print(rand_list)
t = time.process_time_ns()
x = sort(rand_list, len(rand_list))
elapsed_time = time.process_time_ns() - t

# lib.printf("%i", x)
#print(sort(rand_list, len(rand_list)))

print(elapsed_time)

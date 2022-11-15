from pysort.lib import sort
from pysort import ffi
from cffi import FFI
import numpy as np
import ctypes
import time
import random

# ff1 = FFI()
# lib = ff1.dlopen()
a = np.array([2, 1, 4, 3, 5,4])

rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(0,100))

t = time.process_time_ns()
print(rand_list)
c_array=ffi.new("int[]",[2, 1, 4, 3, 5,4])
x = sort(rand_list, len(rand_list))
#print(x)
#print(x[11])
# lib.printf("%i", x)
#print(sort(rand_list, len(rand_list)))
elapsed_time = time.process_time_ns() - t

print(elapsed_time)

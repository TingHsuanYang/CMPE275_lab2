import random
import sort_Test
import time

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(0, n))

arrlen = len(rand_list)
t = time.process_time_ns()
sort_Test.quickSort(rand_list, 0, arrlen-1)
elapsed_time = time.process_time_ns() - t
print("Elapsed time (ns)")
print(elapsed_time)

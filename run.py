import sort_Test	
import time
a = [1, 7, 4, 1, 10, 9, -2]
arrlen = len(a)
t = time.process_time_ns()
sort_Test.quickSort(a,0,arrlen-1)
elapsed_time = time.process_time_ns() - t
print("Elapsed time (ns)")
print (elapsed_time)

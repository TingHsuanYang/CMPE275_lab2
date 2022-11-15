import random
import time


def sub_partition(array, start, end, idx_pivot):
    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)


if __name__ == '__main__':

    # Sample data for our call:
    k = 10
    x = random.sample(range(0, k), k)
    y = x.copy()
    start_time = time.time_ns()
    quicksort(y)
    end_time = time.time_ns()

    print(f"    In Python: array: {x} return sorted array {y[:]}")
    print("--- %s ns ---" % (end_time - start_time))

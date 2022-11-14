from __future__ import print_function


def partition(numbers, low, high):
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] <= pivot:
            i = i + 1
            (numbers[i], numbers[j]) = (numbers[j], numbers[i])
    (numbers[i + 1], numbers[high]) = (numbers[high], numbers[i + 1])
    return i + 1
 

 
def quickSort(numbers, low, high):
    if low < high:
        pi = partition(numbers, low, high)
        quickSort(numbers, low, pi - 1)
        quickSort(numbers, pi + 1, high)
 

import random

from insertion_sort import InsertionSort
from quick_sort import QuickSort
from merge_sort import MergeSort
from heap_sort import HeapSort
from quick_insertion_sort import QuickInsertionSort


size = 100000
a = []
for i in range(0, size):
    a.append(random.randint(0, 1000))

print(a)
QuickInsertionSort(a)
print(a)

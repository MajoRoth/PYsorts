import random

from insertion_sort import InsertionSort
from quick_sort import QuickSort
from merge_sort import MergeSort
from heap_sort import HeapSort
from quick_insertion_sort import QuickInsertionSort
from linear_sorts import CountingSort


size = 20
a = []
for i in range(0, size):
    a.append(random.randint(0, 10))

print(a)
print(CountingSort(a, 11))

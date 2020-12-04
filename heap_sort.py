"""
    Python Implementation of Heap Sort
    using max-heap data type.

    -Time Complexity-
    Best Case: O(n log(n))
    Average Case: O(n log(n))
    Worst Case: O(n log(n))

    Space Complexity: O(n)
"""
import math
heap_size = 0  # global variable


def HeapSort(A):
    global heap_size
    BuildMaxHeap(A)
    for i in range(len(A), 1, -1):
        A[0], A[i-1] = A[i-1], A[0]
        heap_size -= 1
        MaxHeapify(A, 1)



"""
    Below algorithms of the Max Heap datatype.
    Max Heaps are represented with a binary tree 
    which for every node i: A[Parent(i)] >= A[i] 
"""


def BuildMaxHeap(A):
    global heap_size
    heap_size = len(A)
    for i in range(math.floor(heap_size/2), 0, -1):
        MaxHeapify(A, i)


def MaxHeapify(A, i):
    global heap_size
    l = Left(i)
    r = Right(i)
    if l <= heap_size and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        MaxHeapify(A, largest)


def Parent(i):
    return math.floor(i/2)


def Right(i):
    return 2*i+1


def Left(i):
    return 2*i


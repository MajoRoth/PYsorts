"""
    combined version of quick sort and insertion sort
    this algorithm maximize the pros of both sorting algorithms
    quick sort sorting the algorithm until the size of the subarray
    is smaller then 20. then insertion sort does the rest.

    -Time Complexity-

"""
from quick_sort import RandomizedPartition
from insertion_sort import InsertionSort


def QuickInsertionSort(A, p=0, r=None):
    """
    p and r represent the list's border.
    if you want to sort the entire list just leave empty
    """
    if r is None:
        r = len(A)-1
    if p < r:
        if r-p < 20:
            InsertionSort(A, p, r)
        else:
            q = RandomizedPartition(A, p, r)
            QuickInsertionSort(A, p, q-1)
            QuickInsertionSort(A, q+1, r)
"""
    Python Implementation of Quick Sort
    with randomized partition

    -Time Complexity-
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)

    Space Complexity: O(1)

"""
import random


def QuickSort(A, p=0, r=None):
    """
    p and r represent the list's border.
    if you want to sort the entire list just leave empty
    """
    if r is None:
        r = len(A)-1
    if p < r:
        q = RandomizedPartition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)


def RandomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]  # pythonic way to swap
    return Partition(A, p, r)


def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]  # pythonic way to swap
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
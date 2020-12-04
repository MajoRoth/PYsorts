"""
    Python Implementation of Quick Sort
    with randomized partition

    -Time Complexity-
    Best Case: O(n log(n))
    Average Case: O(n log(n))
    Worst Case: O(n log(n))

    Space Complexity: O(n)
"""
import math
import sys


def MergeSort(A, p=0, r=None):
    """
    p and r represent the list's border.
    if you want to sort the entire list just leave empty
    """
    if r is None:
        r = len(A)-1
    if p < r:
        q = math.floor((p+r)/2)
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    n = q-p+1
    m = r-q
    L = []
    R = []
    for i in range(1, n+1):
        L.append(A[p+i-1])
    for j in range(1, m+1):
        R.append(A[q+j])
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

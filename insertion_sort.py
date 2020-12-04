"""
    Python Implementation of Insertion Sort

    -Time Complexity-
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)

    Space Complexity: O(1)

"""


def InsertionSort(A, p=0, r=None):
    if r is None:
        r = len(A)-1
    for j in range(p+1, r+1):
        key = A[j]
        i = j-1
        while i >= p and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


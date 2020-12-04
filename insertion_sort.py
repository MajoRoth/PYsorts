"""
    Python Implementation of Insertion Sort

    -Time Complexity-
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)

    Space Complexity: O(1)

"""
def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


"""
    Few implementation of linear sorts.
    of course every sort has a trade of.
"""


def CountingSort(A, k):
    """
        Counting Sort.
        A contains only integers that are smaller then k

        Time Complexity: O(n+k)
        use this algorithm if k=O(n)

        Space Complexity: O(n)

        IMPORTANT: note that CountingSort DOES NOT change the list A
        but returns a new list.
    """
    B = []
    C = []
    for i in range(0, len(A)):
        B.append(0)
    for i in range(0, k+1):
        C.append(0)
    for i in range(0, len(A)):
        C[A[i]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B



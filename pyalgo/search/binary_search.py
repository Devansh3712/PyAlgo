"""
module for implementation
of binary search
algorithm
"""

def binary_search(arr: list, start: int, end: int, key):

    """
    Binary search implementation
    using iterative method
    """

    while (start <= end):

        mid = int(start + ((end - start) / 2))

        if (arr[mid] < key):
            start = mid + 1

        elif arr[mid] > key:
            end = mid - 1

        else:
            return mid

    return -1

"""
PyAlgo
Devansh Singh, 2021
"""

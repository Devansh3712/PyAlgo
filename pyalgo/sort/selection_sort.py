"""
module for implementation
of selection sort using
iterative method
"""

def selection_sort(arr: list):

    """
    Time Complexity: O(n ^ 2)
    """

    for i in range (len(arr)):

        index = i

        for j in range (i + 1, len(arr)):

            if arr[index] > arr[j]:
                index = j

        arr[i], arr[index] = arr[index], arr[i]

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

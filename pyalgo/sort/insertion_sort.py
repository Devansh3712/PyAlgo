"""
module for implementation
of insertion sort
"""

def insertion_sort(arr: list):

    """
    Time Complexity: O(n ^ 2)
    """

    for i in range (1, len(arr)):

        key = arr[i]
        j   = i - 1

        while (j >= 0 and key < arr[j]):

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

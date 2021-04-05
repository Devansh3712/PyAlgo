"""
module for implementation
of ternary search
algorithm
"""

def ternary_search(arr: list, start: int, end: int, key):

    """
    Ternary search
    using recursive method
    """

    if (start <= end):

        midFirst    = int(start + (end - start) / 3)
        midSecond   = int(midFirst + (end - start) / 3)

        if (arr[midFirst] == key):
            return midFirst

        if (arr[midSecond] == key):
            return midSecond

        if (key < arr[midFirst]):
            return ternary_search(arr, start, midFirst - 1, key)

        return ternary_search(arr, midFirst + 1, midSecond - 1, key)

    return -1

"""
PyAlgo
Devansh Singh, 2021
"""

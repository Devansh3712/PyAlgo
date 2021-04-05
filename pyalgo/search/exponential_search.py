"""
module for implementation
of exponential search
algorithm
"""

from pyalgo.search.binary_search import *

def exponential_search(arr: list, start: int, end: int, key):

    """
    Exponential search using
    iterative moethod
    """

    if (end - start <= 0):

        return -1

    num = 1

    while (num < end - start):
        
        if (arr[num] < key):
            num *= 2

        else:
            break

    return binary_search(arr, int(num / 2), num, key)

"""
PyAlgo
Devansh Singh, 2021
"""

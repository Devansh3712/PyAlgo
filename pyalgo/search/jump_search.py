"""
module for implementation
of exponential search
algorithm
"""

def jump_search(arr: list, key):

    """
    Jump search using
    iterative method
    """

    size    = len(arr)
    start   = 0
    end     = int(size ** 0.5) - 1

    while (arr[end] <= key and end < size):

        start = end
        end += int(size ** 0.5)

        if (end > size - 1):
            end = size

    for i in range (start, end):

        if (arr[i] == key):
            return i

    return -1

"""
PyAlgo
Devansh Singh, 2021
"""

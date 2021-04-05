"""
module for implementation
of efficient method of
bubble sort
"""

def bubble_sort(arr: list):

    """
    Time Complexity: 
    - O(n * n) : worst
    - O(n) : best
    """

    for i in range (len(arr)):

        swap = False

        for j in range (0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        if (swap == False):
            break

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

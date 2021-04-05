"""
module for implementation of
shell sort
"""

def shell_sort(arr: list):

    n       = len(arr)
    gap     = n // 2

    while (gap > 0):

        for i in range (gap, n):

            temp    = arr[i]
            j       = i

            while (j >= gap and arr[j - gap] > temp):

                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

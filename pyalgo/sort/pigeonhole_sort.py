"""
module for implementation
of pigeonhole sort
"""

def pigeonhole_sort(arr: list):

    my_min  = min(arr)
    my_max  = max(arr)
    size    = my_max - my_min + 1
    holes   = [0] * size

    for x in arr:

        holes[x - my_min] += 1

    i = 0
    for count in range(size):

        while (holes[count] > 0):

            holes[count] -= 1
            arr[i] = count + my_min
            i += 1

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

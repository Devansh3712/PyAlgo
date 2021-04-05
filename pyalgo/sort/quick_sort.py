"""
module for implementation of
quick sort
"""

def partition(arr: list, low: int, high: int):
	i = low - 1
	x = arr[high]

	for j in range(low, high):

		if (arr[j] <= x):

			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1] 
	return (i + 1)
 
def quick_sort(arr: list, low: int, high: int):

    """
    iterative implementation
    of quick sort
    """

    size    = high - low + 1
    stack   = [0] * (size)

    top = -1

    top         = top + 1
    stack[top]  = low
    top         = top + 1
    stack[top]  = high

    while (top >= 0):

        high    = stack[top] 
        top     = top - 1
        low     = stack[top] 
        top     = top - 1

        p = partition(arr, low, high) 

        if (p - 1 > low):

            top         = top + 1
            stack[top]  = low
            top         = top + 1
            stack[top]  = p - 1

        if (p + 1 < high):

            top         = top + 1
            stack[top]  = p + 1
            top         = top + 1
            stack[top]  = high

    return arr

def quick_sort_recursive(arr: list, low: int, high: int):

    """
    recursive implementation
    of quick sort
    """

    if (low < high):
  
        pi = partition(arr, low, high)
 
        quick_sort_recursive(arr, low, pi-1)
        quick_sort_recursive(arr, pi + 1, high)

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

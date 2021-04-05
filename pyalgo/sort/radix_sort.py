"""
module for implementation of
radix sort
"""

def count_sort(arr: list, exp1: int):

	n       = len(arr)
	output  = [0] * (n)
	count   = [0] * (10)

	for i in range(0, n):

		index = (arr[i] / exp1)
		count[int(index % 10)] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1

	while (i >= 0):

		index = (arr[i] / exp1)
		output[count[int(index % 10)] - 1] = arr[i]
		count[int(index % 10)] -= 1
		i -= 1

	i = 0
	for i in range(0, len(arr)): 
		arr[i] = output[i] 

def radix_sort(arr: list): 
 
	max1    = max(arr)
	exp     = 1

	while (max1 / exp > 0):

		count_sort(arr, exp)
		exp *= 10

	return arr

"""
PyAlgo
Devansh Singh
"""

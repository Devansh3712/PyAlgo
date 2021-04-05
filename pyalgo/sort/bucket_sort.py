"""
module for implementation
of bucket sort
"""

from pyalgo.sort.insertion_sort import insertion_sort	 
			
def bucket_sort(arr: list):

    l           = []
    slot_num    = 10

    for i in range(slot_num): 
        l.append([]) 

    for j in arr:

        index_b = int(slot_num * j)
        l[index_b].append(j)

    for i in range(slot_num):
        l[i] = insertion_sort(l[i])

    k = 0
    for i in range(slot_num):

        for j in range(len(l[i])):

            arr[k] = l[i][j]
            k += 1

    return arr

"""
PyAlgo
Devansh Singh, 2021
"""

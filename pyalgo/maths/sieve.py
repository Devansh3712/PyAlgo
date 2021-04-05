"""
module for calculating
prime numbers upto 'n'
using sieve of
eratosthenes
"""

def sieve(n: int):

    """
    Using the sieve of eratosthenes
    return an array of all prime
    numbers upto n efficiently
    """

    num1    = (n - 1) // 2
    num2    = 0
    num3    = 3
    arr     = [True] * num1
    result  = [2]

    while ((num3 ** 2) < n):

        if arr[num2]:

            result.append(num3)
            num4 = 2 * num2 * num2 + 6 * num2 + 3

            while (num4 < num1):

                arr[num4]   = False
                num4        = num4 + 2 * num2 + 3

        num2 += 1
        num3 += 2

    while (num2 < num1):

        if arr[num2]:
            result.append(num3)
        
        num2 += 1
        num3 += 2

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

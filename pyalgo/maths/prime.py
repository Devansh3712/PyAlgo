"""
module for checking whether
a given number is prime or
not
"""

def prime(n: int):

    """
    Checking if the number has any
    factors in the range [2, sqrt(n)]
    else it is prime
    """

    if (n == 2):
        return True

    result = True

    for i in range (2, int(n ** 0.5)):

        if (n % i == 0):
            result = False
            break

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

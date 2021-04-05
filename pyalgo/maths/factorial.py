"""
module for calculating
factorials of large
numbers efficiently
"""

def factorial(n: int):

    """
    Calculating factorial using
    prime decomposition
    """

    prime   = [True] * (n + 1)
    result  = 1

    for i in range (2, n + 1):

        if (prime[i]):

            j = 2 * i

            while (j <= n):

                prime[j] = False
                j += i

            sum     = 0
            num     = i

            while (num <= n):

                sum += n // num
                num *= i

            result *= i ** sum

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

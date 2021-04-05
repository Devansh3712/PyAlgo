"""
module for calculating
the nth catalan number
"""

def binomial_coeff(n: int, k: int):

    if (k > n - k):
        k = n - k

    result = 1

    for i in range (k):
        result *= (n - i)
        result /= (i + 1)

    return result

def catalan(n: int):

    """
    Using binomial coefficients
    calculating the nth
    catalan number
    """

    result = binomial_coeff(2 * n, n)
    answer = int(result / (n + 1))

    return answer

"""
PyAlgo
Devansh Singh, 2021
"""

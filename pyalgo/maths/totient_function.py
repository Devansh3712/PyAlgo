"""
module for calculation
the eulers totient
function for n
"""

def totient(n: int):

    result  = n
    num     = 2

    while (num * num <= n):

        if (n % num == 0):

            while (n % num == 0):
                n = int(n / num)

            result -= int(result / num)

        num += 1

    if (n > 1):
        result -= int(result / n)

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

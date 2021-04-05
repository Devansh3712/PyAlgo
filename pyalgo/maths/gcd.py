"""
module for calculating
greatest common divisor (GCD)
and lowest common multiple
(LCM)
"""

def gcd(x: int, y: int):

    """
    Calculating GCD of x and y
    using Euclid's algorithm
    """

    if (x > y):

        while (y != 0):

            x, y = y, x % y

        return x

    else:

        while (x != 0):

            y, x = x, y % x

        return y

def lcm(x: int, y: int):

    """
    Calculating LCM of x and y
    using the formula
    LCM * GCD = x * y
    """

    result = (x * y) // gcd(x, y)
    return result

"""
PyAlgo
Devansh Singh, 2021
"""

"""
module for calculating
bit pattern from 0 to
2 ** n - 1
"""

def gray_code(n: int):

    if (n <= 0):
        return

    result = []
    result.append("0")
    result.append("1")

    num1 = 2

    while (True):

        if (num1 >= 1 << n):
            break

        for j in range (num1 - 1, -1, -1):
            result.append(result[j])

        for j in range (num1):
            result[j] = "0" + result[j]

        for j in range (num1, 2 * num1):
            result[j] = "1" + result[j]

        num1 = num1 << 1

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

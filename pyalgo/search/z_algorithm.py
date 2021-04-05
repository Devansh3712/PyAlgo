"""
module for implementation
of Z algorithm for
pattern matching
"""

def z_arr(string: str, z: list):

    """
    fills z array for given
    string
    """

    len_str = len(string)
    l, r, k = 0, 0, 0

    for i in range (1, len_str):

        if (i > r):

            l, r = i, i

            while (r < len_str and string[r - l] == string[r]):
                r += 1

            z[i] = r - l
            r -= 1

        else:

            k = i - l

            if (z[k] < r - i + 1):
                z[i] = z[k]

            else:

                l = i

                while (r < len_str and string[r - l] == string[r]):
                    r += 1

                z[i] = r - l
                r -= 1

def z_algorithm(text: str, pattern: str):

    """
    returns all occurences
    of pattern in the given
    text
    """

    result      = []
    concat      = pattern + "$" + text
    len_con     = len(concat)
    z           = [0] * len_con

    z_arr(concat, z)

    for i in range (len_con):

        if (z[i] == len(pattern)):
            result.append(i - len(pattern) - 1)

    return result

"""
PyAlgo
Devansh Singh, 2021
"""

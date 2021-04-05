"""
module for implementation
of KMP algorithm for
pattern searching
"""

def kmp(pattern: str, text: str):

    """
    searches all occurences
    of pattern in text, returns
    list of indexes
    """

    len_pat = len(pattern)
    len_txt = len(text)

    arr     = [0] * len_pat
    num1    = 0

    compute(pattern, len_pat, arr)
    num2    = 0
    result  = []

    while (num2 < len_txt):

        if (pattern[num1] == text[num2]):
            num2 += 1
            num1 += 1

        if (num1 == len_pat):
            result.append(num2 - num1)
            num1 = arr[num1 - 1]

        elif (num2 < len_txt and pattern[num1] != text[num2]):

            if (num1 != 0):
                num1 = arr[num1 - 1]

            else:
                num2 += 1

    return result

def compute(pattern: str, len_pat: int, arr: list):

    num1    = 0
    arr[0]  = 0
    num2    = 1

    while (num2 < len_pat):

        if (pattern[num2] == pattern[num1]):

            num1 += 1
            arr[num2] = num1
            num2 += 1

        else:

            if (num1 != 0):
                num1 = arr[num1 - 1]

            else:
                arr[num2] = 0
                num2 += 1

"""
PyAlgo
Devansh Singh, 2021
"""

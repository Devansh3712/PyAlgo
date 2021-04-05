"""
basic template for
competitive programming
"""

import sys

def scanf(datatype = str):

    """
    faster input using
    stdin.readline
    """

    if datatype is not None:
        return datatype(sys.stdin.readline())

    else:
        return sys.stdin.readline()

def printf(answer):

    """
    faster output using
    stdout.write
    """

    return sys.stdout.write(str(answer) + "\n")

def map_input(datatype = str):

    """
    multiple variable input
    in a single line
    """

    return map(datatype, sys.stdin.readline().split())

def list_input(datatype = str):

    """
    list input using map
    function
    """
    return list(map(datatype, sys.stdin.readline().split()))

def testcase(number: int, solve_function):

    """
    run the code for n
    testcases, provided the
    solve function
    """

    while (number != 0):
        solve_function()
        number -= 1

"""
PyAlgo
Devansh Singh, 2021
"""

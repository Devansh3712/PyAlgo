"""
template for testing
modules using unittest
"""

import datetime

function    = input("Enter name of function: ")
filename    = "test_" + function + ".py"
file        = open(filename, 'w')
module_name = input("Enter module name: ")
arguments   = input("Enter the arguments: ")
answer      = input("Enter the answer: ")
name        = input("Name of tester: ")

function_class = ''

if "_" in function:
    function_class = function.replace("_", "").title()

else:
    function_class = function.title()

template = f"""
'''
module for testing
{module_name}.py from
pyalgo math module
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from {module_name} import {function}

class Test{function_class}(unittest.TestCase):

    def test_{function}(self):
        result = {function}({arguments})

        self.assertEqual(result, {answer})

if __name__ == "__main__":
    unittest.main()

'''
PyAlgo
{name}, {datetime.datetime.now().year}
'''
"""

file.write(template)
file.close()

"""
PyAlgo
Devansh Singh, 2021
"""

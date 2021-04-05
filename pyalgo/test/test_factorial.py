"""
module for testing
maths.factorial.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        result = factorial(6)

        self.assertEqual(result, 720)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

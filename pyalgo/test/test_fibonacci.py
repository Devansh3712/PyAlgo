"""
module for testing
maths.fibonacci_numbers.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.fibonnaci_numbers import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        result = fibonacci(6)

        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

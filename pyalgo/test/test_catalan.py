"""
module for testing
maths.catalan_numbers.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.catalan_numbers import catalan

class TestCatalan(unittest.TestCase):

    def test_catalan_number(self):
        result = catalan(6)

        self.assertEqual(result, 132)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

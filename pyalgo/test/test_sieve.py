"""
module for testing
maths.sieve.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.sieve import sieve

class TestSieve(unittest.TestCase):

    def test_sieve(self):
        result = sieve(30)

        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""
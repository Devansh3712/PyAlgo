
"""
module for testing
search.kmp_algorithm.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.kmp_algorithm import kmp

class TestKmp(unittest.TestCase):

    def test_kmp(self):
        result = kmp('ABC', 'ABCABBABC')

        self.assertEqual(result, [0, 6])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

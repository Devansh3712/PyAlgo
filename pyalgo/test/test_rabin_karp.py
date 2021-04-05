
"""
module for testing
search.rabin_karp.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.rabin_karp import rabin_karp

class TestRabinkarp(unittest.TestCase):

    def test_rabin_karp(self):
        result = rabin_karp('ABC', 'ABCABBABC')

        self.assertEqual(result, [0, 6])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

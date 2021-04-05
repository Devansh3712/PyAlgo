
"""
module for testing
search.binary_search.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.binary_search import binary_search

class TestBinarysearch(unittest.TestCase):

    def test_binary_search(self):
        result = binary_search([2, 3, 4, 5], 0, 4, 4)

        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

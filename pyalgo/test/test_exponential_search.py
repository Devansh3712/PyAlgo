
"""
module for testing
search.exponential_search.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.exponential_search import exponential_search

class TestExponentialsearch(unittest.TestCase):

    def test_exponential_search(self):
        result = exponential_search([2, 3, 4, 5], 0, 4, 4)

        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

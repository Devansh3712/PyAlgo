
"""
module for testing
search.jump_search.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.jump_search import jump_search

class TestJumpsearch(unittest.TestCase):

    def test_jump_search(self):
        result = jump_search([2, 3, 4, 5], 4)

        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""


"""
module for testing
sort.quick_sort.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from sort.quick_sort import quick_sort, quick_sort_recursive

class TestQuicksort(unittest.TestCase):

    def test_quick_sort(self):
        result = quick_sort([3, 5, 4, 1, 2], 0, 4)

        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_quick_sort_recursive(self):
        result = quick_sort_recursive([3, 5, 4, 1, 2], 0, 4)

        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""


"""
module for testing
sort.bucket_sort.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from sort.bucket_sort import bucket_sort

class TestBucketsort(unittest.TestCase):

    def test_bucket_sort(self):
        result = bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])

        self.assertEqual(result, [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

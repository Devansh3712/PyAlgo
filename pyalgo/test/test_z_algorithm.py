
"""
module for testing
search.z_algorithm.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from search.z_algorithm import z_algorithm

class TestZalgorithm(unittest.TestCase):

    def test_z_algorithm(self):
        result = z_algorithm('ABCABBABC', 'ABC')

        self.assertEqual(result, [0, 6])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

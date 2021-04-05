"""
module for testing
maths.gcd.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.gcd import gcd, lcm

class TestGcd(unittest.TestCase):

    def test_gcd(self):
        result = gcd(4, 16)

        self.assertEqual(result, 4)

    def test_lcm(self):
        result = lcm(4, 16)

        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

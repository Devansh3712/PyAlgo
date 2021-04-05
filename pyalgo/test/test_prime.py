
"""
module for testing
maths.prime.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.prime import prime

class TestPrime(unittest.TestCase):

    def test_prime(self):
        result = prime(7)

        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

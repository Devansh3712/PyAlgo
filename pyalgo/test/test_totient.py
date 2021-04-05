
"""
module for testing
maths.totient_function.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.totient_function import totient

class TestTotient(unittest.TestCase):

    def test_totient(self):
        result = totient(22)

        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

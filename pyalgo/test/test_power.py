"""
module for testing
maths.power.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.power import big_power, mod_power

class TestPower(unittest.TestCase):

    def test_big_power(self):
        result = big_power(23, 12)

        self.assertEqual(result, 21914624432020321)

    def test_mod_power(self):
        result = mod_power(23, 12, 10 ** 9 + 7)

        self.assertEqual(result, 278617953)

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

"""
module for testing
maths.gray_code.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.gray_code import gray_code

class TestGrayCode(unittest.TestCase):

    def test_gray_code(self):
        result = gray_code(3)

        self.assertEqual(result, ['000', '001', '011', '010', '110', '111', '101', '100'])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

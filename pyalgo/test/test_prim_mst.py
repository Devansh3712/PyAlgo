
"""
module for testing
graph.mst.prim_mst.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from graph.mst.prim_mst import *

class TestPrimmst(unittest.TestCase):

    def test_prim_mst(self):
        g = Graph(5)
        g.graph = [ [0, 2, 0, 6, 0],
                    [2, 0, 3, 8, 5],
                    [0, 3, 0, 0, 7],
                    [6, 8, 0, 0, 9],
                    [0, 5, 7, 9, 0]
                ]
        result = g.prim_mst()

        self.assertEqual(result, {(0, 1): 2, (1, 2): 3, (0, 3): 6, (1, 4): 5})

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

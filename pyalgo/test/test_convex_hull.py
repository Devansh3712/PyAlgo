
"""
module for testing
maths.convex_hull.py from
pyalgo math module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from maths.convex_hull import *

class TestConvexhull(unittest.TestCase):

    def test_convex_hull(self):

        points = []
        points.append(Point(0, 3))
        points.append(Point(2, 2))
        points.append(Point(1, 1))
        points.append(Point(2, 1))
        points.append(Point(3, 0))
        points.append(Point(0, 0))
        points.append(Point(3, 3))
        result = convex_hull(points, len(points))

        self.assertEqual(result, [(0, 3), (0, 0), (3, 0), (3, 3)])

if __name__ == "__main__":
    unittest.main()

"""
PyAlgo
Devansh Singh, 2021
"""

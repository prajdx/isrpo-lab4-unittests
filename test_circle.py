import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(7)
        self.assertAlmostEqual(res, math.pi * 49)

    def test_area_negative(self):
        res = area(-9)
        self.assertAlmostEqual(res, 0)

    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 2 * math.pi * 3)

    def test_perimeter_negative(self):
        res = perimeter(-5)
        self.assertAlmostEqual(res, 0)
        
import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(8, 3)
        self.assertEqual(res, 12.0)

    def test_area_negative(self):
        res = area(-6, 4)
        self.assertEqual(res, 0)

    
    def test_perimeter_normal(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_with_zero(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_perimeter_negative_side(self):
        res = perimeter(-3, 4, 5)
        self.assertEqual(res, 0)

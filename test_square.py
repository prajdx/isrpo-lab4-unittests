import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_negative(self):
        res = area(-5)
        self.assertEqual(res, 0)

    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_negative(self):
        res = perimeter(-5)
        self.assertEqual(res, 0)

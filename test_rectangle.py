import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(5, 7)
        self.assertEqual(res, 35)

    def test_area_square(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_area_negative(self):
        res = area(-5, 7)
        self.assertEqual(res, 0)


    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_normal(self):
        res = perimeter(5, 7)
        self.assertEqual(res, 24)

    def test_perimeter_negative(self):
        res = perimeter(-5, 7)
        self.assertEqual(res, 0)

import unittest
from math import pi
from mindboxtimonin import timtest


class TestTriangle(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(Exception):
            timtest.Triangle(-1, 2, c=2)

    def test_sides(self):
        with self.assertRaises(Exception):
            timtest.Triangle(1, 2, c=3)

    def test_square(self):
        self.assertEqual(timtest.Triangle(3, 4, 5).count_square(), 6)
    
    def test_right(self):
        self.assertTrue(timtest.Triangle(3, 4, 5).is_right())
        self.assertFalse(timtest.Triangle(3, 4, 6).is_right())


class TestCircle(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(Exception):
            timtest.Circle(-3)

    def test_square(self):
        self.assertEqual(timtest.Circle(r=3).count_square(), 9*pi)


class TestDefenition(unittest.TestCase):
    def test_line(self):
        with self.assertRaises(Exception):
            timtest.calculate_square(1, 2)

    def test_triangle(self):
        self.assertEqual(timtest.calculate_square(3, 4, 5), 6)

    def test_triangle(self):
        self.assertEqual(timtest.calculate_square(3), 9*pi)


if __name__ == '__main__':
    unittest.main()

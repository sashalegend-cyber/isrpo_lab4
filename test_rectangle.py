import unittest
from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area_zero_first_side(self):
        self.assertEqual(area(0, 5), 0)

    def test_area_zero_second_side(self):
        self.assertEqual(area(4, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(4, 4), 16)

    def test_area_rectangle(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_commutative(self):
        self.assertEqual(area(2, 7), area(7, 2))

    def test_area_float_arguments(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)


class RectanglePerimeterTestCase(unittest.TestCase):
    """Тесты для функции perimeter."""

    def test_perimeter_zero_first_side(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_zero_second_side(self):
        self.assertEqual(perimeter(4, 0), 8)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(4, 4), 16)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(4, 5), 18)

    def test_perimeter_commutative(self):
        self.assertEqual(perimeter(2, 7), perimeter(7, 2))

    def test_perimeter_float_arguments(self):
        self.assertAlmostEqual(perimeter(2.5, 4.0), 13.0)


if __name__ == "__main__":
    unittest.main()

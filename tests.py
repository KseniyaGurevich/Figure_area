import unittest
import math

from area import calculate_circle_area, calculate_triangle_area, figure_type


class TestGeometryFunctions(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(calculate_circle_area(2), round(4 * math.pi, 2))
        self.assertEqual(calculate_circle_area(0), 0)
        self.assertEqual(calculate_circle_area(5), round(25 * math.pi, 2))

    def test_triangle_area(self):
        self.assertEqual(calculate_triangle_area(3, 4, 5), 6.0)
        self.assertEqual(calculate_triangle_area(7, 24, 25), 84.0)
        self.assertEqual(calculate_triangle_area(1, 1, 1),
                         round(math.sqrt(3) / 4, 2))

        with self.assertRaises(ValueError):
            calculate_triangle_area(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
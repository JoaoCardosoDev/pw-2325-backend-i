import unittest
from circle import Circle

class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle(radious=2)

    def test_calculate_area(self):
        area = self.circle.get_area
        self.assertEqual(round(area, 3), 12.566)

    def test_calculate_circ(self):
        circ = self.circle.get_circ
        self.assertEqual(round(circ, 3), 12.566)

    def test_calculate_diameter(self):
        diameter = self.circle.get_diameter
        self.assertEqual(diameter, 4)

if __name__ == "__main__":
    unittest.main()
    
from circle import *

def test_calculate_area(self):
    area = Circle(radious=2)
    assert area == (round(area, 3), 12.566)

def test_calculate_circ(self):
    circ = Circle(radious=2).get_circ()
    self.assertEqual(round(circ, 3), 12.566)

def test_calculate_diameter(self):
    diameter = self.circle.get_diameter
    self.assertEqual(diameter, 4)
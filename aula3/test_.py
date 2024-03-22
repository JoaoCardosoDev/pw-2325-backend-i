import pytest
from logic import *
import unittest

def sum(a:int, b:int)->int:
    return a+b

@pytest.mark.parametrize(
    argnames="a,b,result",
    argvalues = [
    (1,2,3),
    (2,2,4)
    ]
)
def test_cenas(a,b,result):
    assert sum(a,b) is result


class AreaPerimeterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.rectangle = Rectangle(width=5, height=7)

    @pytest.mark.parametrize(
            argnames="a, result",
            argvalues = [
                (1, b),
                ()
            ]
    )
    def test_calculate_area(self):
        area = self.rectangle.get_area()
        self.assertEqual(area,35)
        assert self.rectangle.get_area() is result

    def test_calculate_perimeter(self):
        perimeter = self.rectangle.get_perimeter()
        assert perimeter ==24

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
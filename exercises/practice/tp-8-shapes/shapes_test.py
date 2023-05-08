import math
import unittest
from typing import List

from shapes import Shape, Circle, Square, Rectangle, Triangle

class ShapesTest(unittest.TestCase):

    def test_sum_shapes_areas(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        total_area: float = Shape.sum_areas(shapes)
        assert math.isclose(total_area, math.pi + 5 + 25 + 43.3, abs_tol=0.1)

    def test_max_shapes_areas(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        max_area: float = Shape.max_area(shapes)
        assert math.isclose(max_area, 43.3, abs_tol=0.1)

    def test_min_shapes_areas(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        min_area: float = Shape.min_area(shapes)
        assert math.isclose(min_area, math.pi, abs_tol=0.1)

    def test_sum_perimeters_areas(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        total_perimeter: float = Shape.sum_perimeters(shapes)
        assert math.isclose(total_perimeter, 2 * math.pi + 12 + 20 + 30, abs_tol=0.1)

    def test_max_shapes_perimeter(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        max_perimeter: float = Shape.max_perimeter(shapes)
        assert math.isclose(max_perimeter, 30, abs_tol=0.1)

    def test_min_shapes_perimeter(self):
        shapes: List[Shape] = [Circle(1), Rectangle(5, 1), Square(5), Triangle(10, 10, 10)]
        min_perimeter: float = Shape.min_perimeter(shapes)
        assert math.isclose(min_perimeter, 2 * math.pi, abs_tol=0.1)

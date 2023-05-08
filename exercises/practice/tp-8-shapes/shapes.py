from __future__ import annotations

import math
from abc import abstractmethod
from typing import List


class Shape:

    def __init__(self):
        pass

    @staticmethod
    def sum_areas(shapes: List[Shape]): pass

    @staticmethod
    def min_area(shapes: List[Shape]): pass

    @staticmethod
    def max_area(shapes: List[Shape]): pass

    @staticmethod
    def sum_perimeters(shapes: List[Shape]): pass

    @staticmethod
    def min_perimeter(shapes: List[Shape]): pass

    @staticmethod
    def max_perimeter(shapes: List[Shape]): pass

    @abstractmethod
    def area(self) -> float: pass

    @abstractmethod
    def perimeter(self) -> float: pass

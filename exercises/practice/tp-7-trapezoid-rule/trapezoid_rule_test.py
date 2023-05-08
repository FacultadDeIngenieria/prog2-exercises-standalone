import math
import unittest

from trapezoid_rule import integrate


class TrapezoidRuleTest(unittest.TestCase):
    def test_constant(self):
        integral = integrate(lambda x: 1, 0, 10, 100)
        self.assertAlmostEqual(10.0, integral, 4)

    def test_x(self):
        integral = integrate(lambda x: x, 0, 10, 100)
        self.assertAlmostEqual((10.0 * 10.0) / 2, integral, 4)

    def test_sin(self):
        integral = integrate(math.sin, 0, 2*math.pi, 1000)
        self.assertAlmostEqual(0, integral, 4)

    def test_ex(self):
        integral = integrate(math.exp, 0, 10, 1000)
        self.assertAlmostEqual(math.exp(10), integral, delta=1)

import unittest

from quadratic_equation import (
    Quadratic
)


# Tests adapted from `problem-specifications//canonical-data.json`


class QuadraticTest(unittest.TestCase):

    def test_roots(self):
        self.assertEquals(Quadratic(2, 0, 0).roots(), (0, 0))
        self.assertEquals(Quadratic(1, 2, 1).roots(), (-1, -1))
        self.assertEquals(Quadratic(1, 1, 1).roots(), ())

    def test_evaluate(self):
        self.assertEquals(Quadratic(1, 1, 1).evaluate(1), 3)
        self.assertEquals(Quadratic(3, 2, 1).evaluate(4), 57)
        self.assertEquals(Quadratic(2.5, 1.3, 8.2).evaluate(2), 2.5 * 2 * 2 + 1.3 * 2 + 8.2)

    def test_to_string(self):
        self.assertEquals(str(Quadratic(1, 2, 3)), "Y = 1 * X2 + 2 * X + 3")
        self.assertEquals(str(Quadratic(4, 2, 1)), "Y = 4 * X2 + 2 * X + 1")

    def test_derivative(self):
        self.assertEquals(Quadratic(1, 2).derivative(), "Y = 2 * X + 2")
        self.assertEquals(Quadratic(3, 4).derivative(), "Y = 6 * X + 4")




if __name__ == "__main__":
    unittest.main()

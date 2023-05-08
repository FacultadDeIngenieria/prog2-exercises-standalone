import unittest

from fraction import (Fraction, gcd)


class FractionTest(unittest.TestCase):
    def test_creation(self):
        f = Fraction(1, 2)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)

    def test_str(self):
        f = Fraction(1, 2)
        self.assertEqual("1/2", str(f))

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 == f2)

    def test_creation_simplifying(self):
        f12 = Fraction(1, 2)
        f24 = Fraction(2, 4)
        self.assertEqual(f12, f24)

    def test_mul(self):
        result = Fraction(1, 2) * Fraction(1, 4)
        self.assertEqual(Fraction(1, 8), result)

    # def test_gcd(self):
    #     self.assertEqual(6, gcd(42, 30))
    #     self.assertEqual(6, gcd(-42, 30))
    #     self.assertEqual(6, gcd(42, -30))

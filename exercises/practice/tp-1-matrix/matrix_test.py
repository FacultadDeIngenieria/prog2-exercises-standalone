import unittest

from matrix import (
    multiply,
)


class MatrixTest(unittest.TestCase):
    def test_empty_matrices(self):
        a = []
        b = []
        c = []
        self.assertEqual(multiply(a, b), c)

    def test_one_by_one(self):
        a = [[1]]
        b = [[1]]
        c = [[1]]
        self.assertEqual(multiply(a, b), c)

    def test_different_dimensions(self):
        a = [[1, 2, 3],
             [4, 5, 6]]

        b = [[1, 2],
             [3, 4],
             [5, 6]]

        c = [[22, 28],
             [49, 64]]

        self.assertEqual(multiply(a, b), c)

    def test_invalid_dimensions(self):
        a = [[1, 2],
             [4, 5]]

        b = [[1, 2],
             [3, 4],
             [5, 6]]

        with self.assertRaises(ValueError) as err:
            multiply(a, b)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Incompatibles dimensions A = 2x2, B = 3x2")

    def test_vectors(self):
        a = [[1, 2, 3]]
        b = [[1], [2], [3]]
        self.assertEqual(multiply(a, b), [[14]])
        self.assertEqual(multiply(b, a), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])

    def test_identity(self):
        identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(multiply(identity, b), b)
        self.assertEqual(multiply(b, identity), b)

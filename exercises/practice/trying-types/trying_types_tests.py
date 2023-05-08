import unittest

from trying_types import (
    sum_lists,
    Dog,
    Vet
)


# Tests adapted from `problem-specifications//canonical-data.json`


class TypingTest(unittest.TestCase):

    def test_sum_lists(self):
        self.assertEqual(sum_lists([]), 0)
        self.assertEqual(sum_lists([[1, 2], [3, 4]]), 10)

    def test_dog(self):
        self.assertTrue(isinstance(Dog().is_alive(), bool))

    def test_vet(self):
        vet = Vet()
        dog = Dog()
        self.assertEqual(dog.is_alive(), vet.study_dog(dog))

    def test_pro_vet(self):
        vet = Vet()
        dog = Dog()
        self.assertEqual(dog.is_alive(), vet.study_dogs([dog]))


if __name__ == "__main__":
    unittest.main()

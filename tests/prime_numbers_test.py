"""Unit tests for prime_numbers module."""

import unittest
from prime_numbers import prime_numbers


class TestPrimeGenerator(unittest.TestCase):
    def test_five(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(5), [2, 3, 5])

    def test_prime_numbers(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_fifty(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_one_hundred(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(100),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97])

    def test_two_hundred(self):
        """Testing if prime numbers are correctly generated."""

        self.assertEqual(prime_numbers(200),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97, 101, 103, 107, 109, 113,
                          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

    def test_one(self):
        """"Testing if one is correctly determined not to be prime."""

        self.assertFalse(prime_numbers(1), "One is not a prime number")

    def test_two(self):
        """Testing if error returned if integer entered is 2."""

        self.assertEqual(prime_numbers(2), [2])

    def test_zero(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertFalse(prime_numbers(0), "Zero is not a prime number")

    def test_invalid_type(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_numbers("String"), "Only integers are allowed.")

    def test_only_positive(self):
        """Testing if error returned if negative integers input."""

        self.assertEqual(prime_numbers(-1), "Not possible to generate prime numbers for integers less than 2.")

        # def test_empty_parameter(self):
        # """Testing if error returned if no input entered."""

        # self.assertEqual(prime_numbers(0), "No number entered.")


if __name__ == "__main__":
    unittest.main()

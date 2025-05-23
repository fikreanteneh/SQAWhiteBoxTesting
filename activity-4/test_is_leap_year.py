import unittest
from is_leap_year_m1 import is_leap_year_mutant


class TestLeapYear(unittest.TestCase):

    def test_1(self):
        self.assertFalse(is_leap_year_mutant(2019))

    def test_2(self):
        self.assertTrue(is_leap_year_mutant(2024))

    def test_3(self):
        self.assertTrue(is_leap_year_mutant(2000))

    def test_4(self):
        self.assertFalse(is_leap_year_mutant(1900))

    def test_5(self):
        self.assertFalse(is_leap_year_mutant(2100))

    def test_6(self):
        self.assertTrue(is_leap_year_mutant(2400))

    def test_7(self):
        self.assertFalse(is_leap_year_mutant(2023))

    def test_8(self):
        self.assertTrue(is_leap_year_mutant(1996))


if __name__ == "__main__":
    unittest.main()

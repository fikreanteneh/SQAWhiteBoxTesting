import unittest
from is_leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):

    def test_path_1(self):
        self.assertFalse(is_leap_year(2019))

    def test_path_2(self):
        self.assertTrue(is_leap_year(2024))

    def test_path_3(self):
        self.assertTrue(is_leap_year(2000))

    def test_path_4(self):
        self.assertFalse(is_leap_year(1900))


if __name__ == "__main__":
    unittest.main()

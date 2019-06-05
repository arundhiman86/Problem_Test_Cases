import unittest
from leap_year import leap

class TestLeapYear(unittest.TestCase):

    def test_year_not_divisible_by_4(self):
        self.assertEqual(leap_check(1997), "Not a leap year")

    def test_year_divisible_by_4_and_100_but_not_by_400(self):
        self.assertEqual(leap_check(1800), "Not a leap year")

    def test_year_divisible_by_4_not_divisible_by_100_and_400(self):
        self.assertEqual(leap_check(1996), "Leap year")

    def test_year_divisible_by_400(self):
        self.assertEqual(leap_check(2000), "Leap year")

if __name__ == '__main__':
    unittest.main()

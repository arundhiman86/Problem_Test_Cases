import unittest
from string_conversion import conversion

class TestStringConversion(unittest.TestCase):

    def test_condition_1(self):
        self.assertEqual(conversion('daBcd', 'ABC'), 'Yes')
    def test_condition_2(self):
        self.assertEqual(conversion('ABcd', 'BCD'), 'No')
    def test_condition_3(self):
        self.assertEqual(conversion('dBcaEbCd', 'EBC'), 'No')
    def test_condition_4(self):
        self.assertEqual(conversion('dbcaEbCd', 'EBC'), 'Yes')
    def test_condition_5(self):
        self.assertEqual(conversion('DCABECD', 'AB'), 'No')
    def test_condition_6(self):
        self.assertEqual(conversion('dAc', 'ABCD'), 'No')
    def test_condition_7(self):
        self.assertEqual(conversion('cdabce', 'DBE'), 'Yes')

if __name__ == '__main__':
    unittest.main()
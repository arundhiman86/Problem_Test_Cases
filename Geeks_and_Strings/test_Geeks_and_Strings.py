'''

Unit test case for Geeks and Strings
'''

import unittest
from geeksandstrings import substring


class TestGeekandStrings(unittest.TestCase):

    # Test to check the normal case
    def test_for_normal_case(self):
        lines = ['abracadabra', 'geeksforgeeks', 'abracadabra', 'geeks',
                 'geeksthrill']
        queries = ['abr', 'geeks', 'geeksforgeeks', 'ge', 'gar']
        res = ['2', '3', '1', '3', '0']
        self.assertEqual(substring(lines, queries), res)

    # Test for case sensitive
    def test_for_upper_case(self):
        lines = ['abracadabra', 'geeksforgeeks', 'abracadabra', 'geeks',
                 'geeksthrill']
        queries = ['ABR', 'geeks', 'geeksforgeeks', 'GE', 'gar']
        res = ['0', '3', '1', '0', '0']
        self.assertEqual(substring(lines, queries), res)

    # Test for same strings
    def test_for_same(self):
        lines = ['abr', 'geeks', 'geeksforgeeks', 'ge',
                 'gar']
        queries = ['abr', 'geeks', 'geeksforgeeks', 'ge', 'gar']
        res = ['1', '2', '1', '3', '1']
        self.assertEqual(substring(lines, queries), res)

    # Test for camel case letters
    def test_for_camel_case(self):
        lines = ['abracadabra', 'geeksforgeeks', 'aBracadabra', 'geeks',
                 'geeksthrill']
        queries = ['abr', 'geeks', 'geeksForgeeks', 'ge', 'gar']
        res = ['1', '3', '0', '3', '0']
        self.assertEqual(substring(lines, queries), res)

    # Test for lower and upper strings
    def test_for_lower_case(self):
        lines = ['ABRACADABRA', 'GEEKSFORGEEKS', 'abracadabra', 'geeks',
                 'geeksthrill']
        queries = ['abr', 'geeks', 'geeksforgeeks', 'ge', 'gar']
        res = ['1', '2', '0', '2', '0']
        self.assertEqual(substring(lines, queries), res)

    # Test for integers as a string in lines
    def test_for_integer_as_string(self):
        lines = ['2', '3', '6', '8', '10']
        queries = ['abr', 'geeks', 'geeksforgeeks', 'ge', 'gar']
        res = ['0', '0', '0', '0', '0']
        self.assertEqual(substring(lines, queries), res)

    # Test for integers as a string in both
    def test_for_complete_integers_as_strings(self):
        lines = ['248', '398745', '60173', '24', '60284']
        queries = ['2', '398', '60173', '24', '60']
        res = ['2', '1', '1', '2', '2']
        self.assertEqual(substring(lines, queries), res)

    # # Test for input as an integer
    # def test_for_integers(self):
    #     lines = [1245, 653, 789, 6856, 101]
    #     queries = [8, 65, 789, 1, 6]
    #     res = ['0', '1', '1', '2', '2']
    #     self.assertEqual(substring(lines, queries), res)


if __name__ == '__main__':
    unittest.main()

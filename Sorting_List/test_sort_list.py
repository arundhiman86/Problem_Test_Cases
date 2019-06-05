import unittest
from sort_list import sort

class testSortingList(unittest.TestCase):

    def test_for_normal_case(self):
        x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
        z = sort(x, y)
        res = ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
        self.assertListEqual(z, res)

    def test_for_opposite_case(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        y = ['a', 'd', 'h', 'b', 'a', 'e', 'i', 'f', 'b']
        z = sort(x, y)
        res = [0, 4, 3, 8, 1, 5, 7, 2, 6]
        self.assertListEqual(z, res)

    def test_for_already_sorted(self):
        x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        y = [0, 0, 1, 1, 2, 3, 4, 5, 6]
        z = sort(x, y)
        res = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.assertListEqual(z, res)

if __name__ == '__main__':
    unittest.main()

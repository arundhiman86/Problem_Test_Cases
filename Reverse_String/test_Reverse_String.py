import unittest

from reverse_string import reverse

class TestReverseString(unittest.TestCase):

    def test_string_with_characters(self):
        self.assertEqual(reverse('common'), "nommoc")

    def test_string_with_numbers(self):
        self.assertEqual(reverse(1998), "8991")

    def test_string_with_float(self):
        self.assertEqual(reverse(34.57), "75.43")

    def test_string_with_spaces(self):
        self.assertEqual(reverse(''), "Empty string")

    def test_string_with_spaces_before_after_and_in_between(self):
        self.assertEqual(reverse(' arun dhiman  '), "namihd nura")

    def test_string_mixed_sequences(self):
        self.assertEqual(reverse('12arun.14dh'), "hd41.nura21")

if __name__ == '__main__':
    unittest.main()

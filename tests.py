import unittest
from check_pwd import check_pwd


class Tests(unittest.TestCase):
    def test_if_less_than_8_characters_then_false(self):
        test_string = "abcde"
        self.assertFalse(check_pwd(test_string))

    def test_if_greater_than_20_characters_then_false(self):
        test_string = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"
        self.assertFalse(check_pwd(test_string))

    def test_if_string_contains_no_lower_case_character_then_false(self):
        test_string = "ABCDEFGHIJK"
        self.assertFalse(check_pwd(test_string))

    def test_if_string_contains_no_upper_case_character_then_false(self):
        test_string = "abcdefhijk"
        self.assertFalse(check_pwd(test_string))

    def test_if_string_contains_no_numbers_then_false(self):
        test_string = "abCdefhijkbac"
        self.assertFalse(check_pwd(test_string))

    def test_if_string_contains_no_symbols_then_false(self):
        test_string = "abCdefhijkbac4"
        self.assertFalse(check_pwd(test_string))

    def test_if_string_contains_unallowed_symbols_then_false(self):
        test_string = "a(bCdjkbac4[]"
        self.assertFalse(check_pwd(test_string))


if __name__ == '__main__':
    unittest.main()

import unittest
from check_pwd import check_pwd


class Tests(unittest.TestCase):
    def test_if_less_than_8_characters_then_false(self):
        test_string = "abcde"
        self.assertFalse(check_pwd(test_string))


if __name__ == '__main__':
    unittest.main()

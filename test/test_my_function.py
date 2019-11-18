from unittest import TestCase

from justatest import my_function

class TestJYF(TestCase):
    def test_my_function(self):
        self.assertEqual(4, my_function(-2))
        self.assertEqual(1, my_function(-1))
        self.assertEqual(0, my_function(0))
        self.assertEqual(1, my_function(1))
        self.assertEqual(4, my_function(2))

from unittest import TestCase

from justatest import your_function

class TestJYF(TestCase):
    def test_your_function(self):
        self.assertEqual(4, your_function(-2))
        self.assertEqual(1, your_function(-1))
        self.assertEqual(0, your_function(0))
        self.assertEqual(1, your_function(1))
        self.assertEqual(4, your_function(2))

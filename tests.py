import unittest
from unittest.mock import MagicMock

import app

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestAppMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(app.my_function(), 'hello')


class TestAppMockMethods(unittest.TestCase):
    def setUp(self):
        app.my_function = MagicMock(return_value="from a magic mock!")

    def test_upper(self):
        self.assertEqual(app.my_function(), 'from a magic mock!')

if __name__ == '__main__':
    unittest.main()
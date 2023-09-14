import unittest
from utils import Utils

class TestReversed(unittest.TestCase):
    def test_string(self):
        self.assertEqual("Input must be an int", Utils.reversed("blah"))
    def test_float(self):
        self.assertEqual("Input must be an int", Utils.reversed(10.67))
    def test_integer(self):
        self.assertEqual(16, Utils.reversed(61))

class TestFormatter(unittest.TestCase):
    def test_string(self):
        self.assertEqual("Input must be an int", Utils.formatter("blah"))
    def test_float(self):
        self.assertEqual("Input must be an int", Utils.formatter(10.67))
    def test_integer(self):
        self.assertEqual("Binary: 111101 Octal: 75", Utils.formatter(61))

if __name__=='__main__':
	unittest.main()
    
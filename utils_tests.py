import unittest
from utils import Utils

class TestReversed(unittest.TestCase):
    def test_string(self):
        util = Utils()
        self.assertEqual("Input must be an int", util.reversed("blah"))
    def test_float(self):
        util = Utils()
        self.assertEqual("Input must be an int", util.reversed(10.67))
    def test_integer(self):
        util = Utils()
        self.assertEqual(16, util.reversed(61))

class TestFormatter(unittest.TestCase):
    def test_string(self):
        util = Utils()
        self.assertEqual("Input must be an int", util.formatter("blah"))
    def test_float(self):
        util = Utils()
        self.assertEqual("Input must be an int", util.formatter(10.67))
    def test_integer(self):
        util = Utils()
        self.assertEqual("Binary: 111101 Octal: 75", util.formatter(61))

if __name__=='__main__':
	unittest.main()
    
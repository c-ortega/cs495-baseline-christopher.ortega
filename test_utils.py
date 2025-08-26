import unittest
from utils import romanConvert

class TestRoman(unittest.TestCase):
    def test_m(self):
        self.assertEqual(romanConvert(1000), "M")
    def test_IV(self):
        self.assertEqual(romanConvert(4), "IV")
    def test_VI(self):
        self.assertEqual(romanConvert(6), "VI")
    def test_XC(self):
        self.assertEqual(romanConvert(90), "XC")

if __name__ == "__main__":
    unittest.main()
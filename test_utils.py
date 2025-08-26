import unittest
from utils import romanConverter

class TestRoman(unittest.TestCase):
    def test_m(self):
        self.assertEqual(romanConverter(1000), "M")
    def test_IV(self):
        self.assertEqual(romanConverter(4), "IV")
    def test_VI(self):
        self.assertEqual(romanConverter(6), "VI")
    def test_XC(self):
        self.assertEqual(romanConverter(90), "XC")

if __name__ == "__main__":
    unittest.main()
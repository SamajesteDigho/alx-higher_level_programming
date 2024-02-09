#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMax(unittest.TestCase):
    """ Test class for the maximum list """

    def test_max(self):
        """ Test for maximum in list """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)


if __name__ == "__main__":
    unittest.main()

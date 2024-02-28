#!/usr/bin/python3
"""Test file for the base class"""
import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Class for the test cases"""

    def setUp(self):
        """Initialization of variables"""
        self.rec1 = Rectangle(10, 2)
        self.rec2 = Rectangle(2, 10)
        self.rec3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """Tearing down"""
        del self.rec1
        del self.rec2
        del self.rec3

    def test_initializations(self):
        self.assertEqual(self.rec1.width, 10)
        self.assertEqual(self.rec2.height, 10)
        self.assertEqual(self.rec3.x, 0)
        self.assertEqual(self.rec1.y, 0)
        self.assertEqual(self.rec3.id, 12)

#!/usr/bin/python3
"""Test file for the base class"""
import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Class for the test cases"""

    def test_initializations(self):
        rec1 = Rectangle(1, 2)
        rec2 = Rectangle(1, 2, 3)
        rec3 = Rectangle(1, 2, 3, 4)
        rec4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.width, 1)
        self.assertEqual(rec2.x, 3)
        self.assertEqual(rec3.y, 4)
        self.assertEqual(rec4.id, 5)
    
    def test_errors(self):
        """Test documentation here we find it"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
            Rectangle(1, "2")
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")
        
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(1, -2)
            Rectangle(0, 2)
            Rectangle(1, 0)
            Rectangle(1, 2, -3)
            Rectangle(1, 2, 3, -4)
        
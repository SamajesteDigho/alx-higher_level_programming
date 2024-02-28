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
        self.assertEqual(rec1.height, 2)
        self.assertEqual(rec2.x, 3)
        self.assertEqual(rec3.y, 4)
        self.assertEqual(rec4.id, 5)
    
    def test_errors(self):
        """Test documentation here we find it"""
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, "1", 2)
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 1, "2")
        self.assertRaisesRegex(TypeError, "x must be an integer", Rectangle, 1, 2, "3")
        self.assertRaisesRegex(TypeError, "y must be an integer", Rectangle, 1, 2, 3, "4")
        
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, -1, 2)
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, 0, 2)
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 1, -2)
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 1, 0)
        self.assertRaisesRegex(ValueError, "x must be >= 0", Rectangle, 1, 2, -3)
        self.assertRaisesRegex(ValueError, "y must be >= 0", Rectangle, 1, 2, 3, -4)

#!/usr/bin/python3
"""Test file for the base class"""
import unittest
import os
from models.square import Square


class BaseModelTestCase(unittest.TestCase):
    """Class for the test cases"""

    def test_intialization(self):
        """Initialization of variables"""
        Square(1)
        Square(1, 2)
        Square(1, 2, 3)
        Square(1, 2, 3, 4)

        self.assertRaisesRegex(TypeError, "width must be an integer", Square,
                               "1")
        self.assertRaisesRegex(TypeError, "x must be an integer", Square,
                               1, "2")
        self.assertRaisesRegex(TypeError, "y must be an integer", Square,
                               1, 2, "3")

        self.assertRaisesRegex(ValueError, "width must be > 0", Square,
                               -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0", Square,
                               1, -2)
        self.assertRaisesRegex(ValueError, "y must be >= 0", Square,
                               1, 2, -3)
        self.assertRaisesRegex(ValueError, "width must be > 0", Square,
                               0)

    def test_basic_functions(self):
        """Test documentation here we find it"""
        sqr1 = Square(1, id=1)
        self.assertEqual(sqr1.__str__(), f"[Square] (1) 0/0 - 1")
        self.assertEqual(sqr1.to_dictionary(), {"id": 1, "size": 1,
                                                "x": 0, "y": 0})
        sqr1.update()
        self.assertEqual(sqr1.to_dictionary(), {"id": 1, "size": 1,
                                                "x": 0, "y": 0})

    def test_advanced_functions(self):
        """Test documentation here we find it"""
        sqr1 = Square(3, id=1)
        sqr1.update()
        self.assertEqual(sqr1.to_dictionary(), {"id": 1, "size": 3,
                                                "x": 0, "y": 0})

        sqr1.update(89)
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 3,
                                                "x": 0, "y": 0})

        sqr1.update(89, 1)
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 0, "y": 0})

        sqr1.update(89, 1, 2)
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 0})

        sqr1.update(89, 1, 2, 3)
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 3})

        sqr1.update(**{"id": 89})
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 3})

        sqr1.update(**{"id": 89, "size": 1})
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 3})

        sqr1.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 3})

        sqr1.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(sqr1.to_dictionary(), {"id": 89, "size": 1,
                                                "x": 2, "y": 3})

        sqr = Square.create(**{"id": 89})
        self.assertEqual(sqr.to_dictionary(), {"id": 89, "size": 1,
                                               "x": 0, "y": 0})

        sqr = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(sqr.to_dictionary(), {"id": 89, "size": 1,
                                               "x": 0, "y": 0})

        sqr = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(sqr.to_dictionary(), {"id": 89, "size": 1,
                                               "x": 2, "y": 0})

        sqr = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(sqr.to_dictionary(), {"id": 89, "size": 1,
                                               "x": 2, "y": 3})

    def test_advanced_functions_files(self):
        """Test documentation here we find it"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

        Square.load_from_file()
        Square.load_from_file()

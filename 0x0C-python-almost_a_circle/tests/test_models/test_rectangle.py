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
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "1", 2)
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 1, "2")
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 1, 2, "3")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 1, 2, 3, "4")

        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -1, 2)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, 0, 2)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 1, -2)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 1, 0)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 1, 2, -3)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 1, 2, 3, -4)

    def test_basic_funcs(self):
        """Test documentation here we find it"""
        rec1 = Rectangle(1, 2, id=1)
        rec2 = Rectangle(1, 2, 3, id=2)
        rec3 = Rectangle(1, 2, 3, 4, id=3)
        self.assertEqual(rec1.area(), 2)
        self.assertIsInstance(rec1.__str__(), str)
        self.assertEqual(rec1.__str__(), "[Rectangle] (1) 0/0 - 1/2")
        self.assertIsNone(rec1.display())
        self.assertIsNone(rec2.display())
        self.assertIsNone(rec3.display())

    def test_advanced_functions_dictionary(self):
        """Test documentation here we find it"""
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(rec1.to_dictionary(), dict)
        self.assertEqual(rec1.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 5})
        rec2 = Rectangle(4, 3, id=1)

        rec2.update(89)
        self.assertEqual(rec2.to_dictionary(), {"width": 4, "height": 3,
                                                "x": 0, "y": 0, "id": 89})

        rec2.update(89, 1)
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 3,
                                                "x": 0, "y": 0, "id": 89})

        rec2.update(89, 1, 2)
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 0, "y": 0, "id": 89})

        rec2.update(89, 1, 2, 3)
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 0, "id": 89})

        rec2.update(89, 1, 2, 3, 4)
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

        rec2.update(**{'id': 89})
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

        rec2.update(**{'id': 89, "width": 1})
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

        rec2.update(**{'id': 89, "width": 1, "height": 2})
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

        rec2.update(**{'id': 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

        rec2.update(**{'id': 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(rec2.to_dictionary(), {"width": 1, "height": 2,
                                                "x": 3, "y": 4, "id": 89})

    def test_advanced_function_create(self):
        """Test documentation here we find it"""
        Rectangle.create(**{"id": 89})
        Rectangle.create(**{"id": 89, "width": 1})
        Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})

    def test_advanced_functions_file(self):
        """Test documentation here we find it"""
        Rectangle.save_to_file(None)
        Rectangle.save_to_file([])
        Rectangle.save_to_file([Rectangle(1, 2)])
        Rectangle.load_from_file()
        Rectangle.load_from_file()

#!/usr/bin/python3
"""Test file for the base class"""
import unittest
from models.base import Base


class BaseModelTestCase(unittest.TestCase):
    """Class for the test cases"""

    def test_initializations(self):
        """Testing correct initialization at id"""
        base1 = Base()
        base2 = Base(12)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 12)

    def test_to_json_string(self):
        """Test documentation here we find it"""
        val1 = Base.to_json_string(None)
        val2 = Base.to_json_string([])
        val3 = Base.to_json_string([{'id': 12}])
        self.assertEqual(val1, "[]")
        self.assertEqual(val2, "[]")
        self.assertEqual(val3, '[{"id": 12}]')

    def test_from_json_string(self):
        """Test documentation here we find it"""
        val1 = Base.from_json_string(None)
        val2 = Base.from_json_string("[]")
        val3 = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(val1, (list))
        self.assertCountEqual(val1, [])
        self.assertIsInstance(val2, (list))
        self.assertCountEqual(val2, [])
        self.assertIsInstance(val3, (list))
        self.assertCountEqual(val3, [{"id": 89}])

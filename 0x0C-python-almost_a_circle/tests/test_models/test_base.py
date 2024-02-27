#!/usr/bin/python3
"""Test file for the base class"""
import unittest
from models.base import Base


class BaseModelTestCase(unittest.TestCase):
    """Class for the test cases"""

    def setUp(self):
        """Initialization of variables"""
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base()
        self.base4 = Base(id=12)
        self.base5 = Base()

    def tearDown(self):
        del self.base1
        del self.base2
        del self.base3
        del self.base4
        del self.base5

    def test_initializations(self):
        """Testing correct initialization at id"""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 3)
        self.assertEqual(self.base4.id, 12)
        self.assertEqual(self.base5.id, 4)

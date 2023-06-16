#!/usr/bin/python3

""" Unittests for base class """

import unittest

from models.base import Base

class TestBase(unittest.TestCase):

    def test_positive_id(self):
        my_obj = Base(10)
        self.assertEqual(my_obj.id, 10)

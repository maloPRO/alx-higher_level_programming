#!/usr/bin/python3

""" Unittest for rectangle class """

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Rectangle class unittest """

    def test_id(self):
        r = Rectangle(10, 9, 0, 0, 11)
        self.assertEqual(r.id, 11)

    def test_sides(self):
        r = Rectangle(10, 8, 4, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            r = Rectangle('one', 10)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 'one')

        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 'one', 3)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 5, 1, 'one')

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(-3, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(3, -9)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 5, -3, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 4, -8)

    def test_area(self):
        r = Rectangle(4, 10)
        self.assertEqual(r.area(), 40)

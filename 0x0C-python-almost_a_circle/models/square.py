#!/usr/bin/python3

""" Defines a square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creates a square """

    def __init__(self, size, x=0, y=0, id=None):

        """ Initializes square """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

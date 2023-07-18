#!/usr/bin/python3
"""contains a class square that inherits from the from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """overrides the __str__ of parent class -Rectangle
        Returns:
            return [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the attributes of the suare object

        Args:
            *args (ints): the list of arguments
            -1st argument should be the id attribute
            -2nd argument should be the size attribute
            -3rd argument should be the x attribute
            -4th argument should be the y attribute

            **kwargs (dict): a dict of key-value arguments
        """
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        result = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
        }
        return result

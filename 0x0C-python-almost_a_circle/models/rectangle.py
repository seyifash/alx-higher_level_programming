#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the objects for the rectangle class

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter methods that gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for the x Attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for the y Attributes"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation that overides the __str__ method

        Return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                type(self).__name__, self.id, self.__x, self.__y, self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """update the rectangle class

        Args:
            *args (ints): new attribute
            -1st argument should be the id attribute
            -2nd argument should be the width attribute
            -3rd argument should be the height attribute
            -4th argument should be the x attribute
            -5th argument should be the y attribute
        """

        count = 0
        for arg in args:
            if count == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif count == 1:
                self.width = arg
            elif count == 2:
                self.height = arg
            elif count == 3:
                self.x = arg
            elif count == 4:
                self.y = arg
            count += 1

        for key, value in kwargs.items():
            tmp = ["id", "width", "height", "x", "y"]
            if key in tmp and tmp.index(key) >= count:
                if key == tmp[0]:
                    if value is None:
                        self.__init__(self.width, self.height, self.x. self.y)
                    self.id = value
                elif key == tmp[1]:
                    self.width = value
                elif key == tmp[2]:
                    self.height = value
                elif key == tmp[3]:
                    self.x = value
                elif key == tmp[4]:
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        result = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
            }
        return result

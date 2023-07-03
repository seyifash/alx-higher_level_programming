#!/usr/bin/python3
"""Contains a rectangle class"""


class Rectangle:
    """A class that defines a rectangle object

    Attributes:
        number_of_instances (int): the number of Rectangle classes
        print_symbol (any): The symbol used to printthe rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
        width (int): The width of the new rectangle
        height (int): the height of the new rectangle
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get and set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get and sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the printable representaion of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """The internal representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """method used to called when the del keyword is called"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with the largest area

        Args:
        rect_1 (Rectangle): the first rectangle
        rect_2 (Rectangle): the second rectangle

        Raises:
        TypeError: if either of rect_1 or rect_2 is not a rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

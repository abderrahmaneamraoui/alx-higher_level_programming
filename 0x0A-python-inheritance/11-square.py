#!/usr/bin/python3

"""
Square #2 module
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value if it is an integer greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns the string representation of the Rectangle object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square object with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the Square object
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

#!/usr/bin/python3
class Square:
    """This class defines a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a square object.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

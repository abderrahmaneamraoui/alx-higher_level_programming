#!/usr/bin/python3

"""
My list module
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        print(sorted(self))

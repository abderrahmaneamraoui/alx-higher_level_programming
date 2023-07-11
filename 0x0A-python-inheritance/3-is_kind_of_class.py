#!/usr/bin/python3

"""
Same class or inherit from module
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class
    """
    return isinstance(obj, a_class)

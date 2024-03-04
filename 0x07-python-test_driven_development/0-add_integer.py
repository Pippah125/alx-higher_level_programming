#!/usr/bin/python3
"""A function  to add two numbers

This function performs the addition operation between two numbers,
these numbers can  either be integers or floats.

"""
def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        raise TypeError("Both a and b must be convertible to integers")

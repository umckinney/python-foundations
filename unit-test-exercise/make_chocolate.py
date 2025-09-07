#!/usr/bin/env python

"""
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).

Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.
"""


def make_chocolate(chocolate_kg):
    """
    Requirements:
        chocolate_kg is an integer
        chocolate_kg % 5 is the count of small bars to return
        Return -1 if
            chocolate_kg = 0
            chocolate_kg is not an integer
    Args:
        chocolate_kg: int of total chocolate in package in kilograms
    Returns:
        count_of_small_bars: int count of 1kg bars of chocolate or -1
    """
    if make_chocolate:  # check if a null value is passed
        if type(make_chocolate) is int:
            if make_chocolate >= 0:
                return make_chocolate % 5
    return -1

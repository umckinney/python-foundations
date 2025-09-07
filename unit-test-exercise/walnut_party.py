#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    """
    Requirements:
        If not is_weekend, 40 <= walnuts <= 60
        If is_weekend, 40 <= walnuts
    Args:
        walnuts: int indicating count of walnuts
        is_weekend: bool indicating weekend status (True = weekend)
    Return:
        successful_party: bool if requirements are met
    """
    if not is_weekend:
        if 40 <= walnuts <= 60:
            return True
    elif is_weekend:
        if 40 <= walnuts:
            return True
    return False

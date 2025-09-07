#!/usr/bin/env python

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.

Else return False
"""


def cat_dog(user_input):
    """
    Requirements:
    Args:
        user_input: any user input
    Returns:
        True if user_input is str AND count 'cat' == count 'dog'
        else False
    """
    if type(user_input) == str:
        if user_input.lower().count("cat") == user_input.lower().count("dog"):
            return True

    return False


if __name__ == "__main__":
    print(cat_dog("catdog"))

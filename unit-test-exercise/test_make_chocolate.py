#!/usr/bin/env python

"""
Test code for the make_chocolate codebat exercise

Adapted from the "coding bat" site: https://codingbat.com/prob/p190859

We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).

Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.
"""


# import the make_chocolate.py function
from make_chocolate import make_chocolate


# simple positive tests to validate results for 1-15
def test_1():  # 1 - 15kg of chocolate is handled
    for _ in range(1, 16):
        assert make_chocolate(_ % 5)


# simple negative test cases for bad input
def test_2():  # 0kg of chocolate is handled
    assert make_chocolate(0) is -1


def test_3():  # alpha string is handled
    assert make_chocolate("abc") is -1


def test_4():  # list is handled
    assert make_chocolate([1, 3, 5]) is -1


def test_5():  # negative numbers are handled
    assert make_chocolate(-2) is -1

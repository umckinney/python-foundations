#!/usr/bin/env python

"""
Test code for the cat_dog codebat exercise

Adapted from the "coding bat" site: https://codingbat.com/prob/p164876

Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""


# import the cat_dog.py function
from cat_dog import cat_dog


# simple positive tests
def test_1():
    assert cat_dog("catdog") is True


def test_2():
    assert cat_dog("1cat1cagogodog") is True


def test_3():
    assert cat_dog("duckgoose") is True


# simple negative test cases for bad input
def test_4():
    assert cat_dog("catcat") is False


def test_5():
    assert cat_dog("dogdog") is False


def test_6():
    assert cat_dog("catdogcatdo") is False


def test_7():
    assert cat_dog(1) is False


def test_8():
    assert cat_dog(["cat", "dog"]) is False

#!/usr/bin/env python

from args_and_kwargs_lab import color_function, color_function_2


def test_defaults():
    assert color_function() == ["black", "white", "blue", "red"]


def test_positionals():
    assert color_function("green", "orange", "brown", "yellow") == [
        "green",
        "orange",
        "brown",
        "yellow",
    ]


def test_keywords():
    assert color_function(fore_color="green", visited_color="green") == [
        "green",
        "white",
        "blue",
        "green",
    ]


def test_positional_and_keywords():
    assert color_function(
        "green", "orange", visited_color="magenta", link_color="eggshell"
    ) == ["green", "orange", "eggshell", "magenta"]


def test_args_kwargs():
    regular = ("pink", "navy")
    links = {"visited_color": "amber", "link_color": "chartruse"}
    assert color_function(*regular, **links) == ["pink", "navy", "chartruse", "amber"]


def test_ak_1():
    regular = ["gold", "silver"]
    links = {"link_color": "bronze", "visited_color": "titanium"}
    print(color_function_2(*regular, **links))
    assert color_function_2(*regular, **links) == [
        "gold",
        "silver",
        "bronze",
        "titanium",
    ]


def test_ak_2():
    regular = ["gold", "silver", "nickel"]
    links = {
        "link_color": "bronze",
        "visited_color": "titanium",
        "revisited_color": "iron",
    }
    print(color_function_2(*regular, **links))
    assert color_function_2(*regular, **links) == [
        "gold",
        "silver",
        "nickel",
        "bronze",
        "titanium",
        "iron",
    ]

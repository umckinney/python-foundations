#!/usr/bin/env python

from magic_methods_circle import Circle, Sphere

"""Circle Unit Tests"""


def test_circle_init():
    test_circle = Circle(4)
    assert test_circle.radius == 4.0


def test_circle_diameter():
    test_circle = Circle(4)
    assert test_circle.diameter() == 8.0


def test_set_circle_diameter():
    test_circle = Circle.from_diameter(10)
    assert test_circle.radius == 5.0


def test_circle_area():
    test_circle = Circle(4)
    assert round(test_circle.area, 2) == 50.27


def test_circle_str():
    test_circle = Circle(5)
    assert str(test_circle) == "Circle with radius 5.0"


def test_circle_repr():
    test_circle = Circle(5)
    assert repr(test_circle) == "Circle(5.0)"


def test_circle_addition():
    test_circle_1 = Circle(2)
    test_circle_2 = Circle(10)
    print(f"test circle 1 + test circle 2 = {test_circle_1 + test_circle_2}")
    assert (test_circle_1 + test_circle_2) == Circle(12)


def test_circle_subtractions():
    test_circle_1 = Circle(12)
    test_circle_2 = Circle(10)
    assert (test_circle_1 - test_circle_2) == Circle(2)


def test_circle_multiplication():
    test_circle_1 = Circle(4)
    test_circle_2 = Circle(5)
    assert (test_circle_1 * test_circle_2) == Circle(20)


def test_circle_division():
    test_circle_1 = Circle(40)
    test_circle_2 = Circle(5)
    assert (test_circle_1 / test_circle_2) == Circle(8)


def test_circle_less_than():
    test_circle_1 = Circle(10)
    test_circle_2 = Circle(20)
    assert (test_circle_1 < test_circle_2) == True


def test_circle_less_than_equal_to():
    test_circle_1 = Circle(10)
    test_circle_2 = Circle(20)
    test_circle_3 = Circle(20)
    assert test_circle_1 < test_circle_2
    assert test_circle_2 <= test_circle_3


def test_circle_equal_to():
    test_circle_1 = Circle(10)
    test_circle_2 = Circle(10)
    assert test_circle_1 == test_circle_2


def test_circle_greater_than():
    test_circle_1 = Circle(20)
    test_circle_2 = Circle(10)
    assert (test_circle_1 > test_circle_2) == True


def test_circle_greater_than_equal_to():
    test_circle_1 = Circle(30)
    test_circle_2 = Circle(20)
    test_circle_3 = Circle(20)
    assert test_circle_1 > test_circle_2
    assert test_circle_2 >= test_circle_3


def test_circle_not_equal_to():
    test_circle_1 = Circle(20)
    test_circle_2 = Circle(10)
    assert test_circle_1 != test_circle_2


def test_circle_sort_list():
    list_of_circles = [Circle(20), Circle(2), Circle(5)]
    list_of_circles.sort()
    assert list_of_circles[0] == Circle(2)
    assert list_of_circles[1] == Circle(5)
    assert list_of_circles[2] == Circle(20)


def test_circle_multiply_by_number():
    test_circle = Circle(2)
    assert (test_circle * 5) == Circle(10)
    assert (5 * test_circle) == Circle(10)
    assert (test_circle * 5) == (5 * test_circle)


"""Sphere Unit Tests"""


def test_sphere_init():
    test_sphere = Sphere(4)
    assert test_sphere.radius == 4.0


def test_sphere_diameter():
    test_sphere = Sphere(4)
    assert test_sphere.diameter() == 8.0


def test_set_sphere_diameter():
    test_sphere = Sphere.from_diameter(10)
    print(f"test_sphere diameter = {test_sphere.diameter()}")
    print(f"test_sphere radius = {test_sphere.radius}")
    assert test_sphere.radius == 5.0


def test_sphere_area():
    test_sphere = Sphere(4)
    assert round(test_sphere.area(), 2) == 201.06


def test_sphere_volume():
    test_sphere = Sphere(2)
    assert round(test_sphere.volume(), 2) == 33.51


def test_sphere_str():
    test_sphere = Sphere(5)
    assert str(test_sphere) == "Sphere with radius 5.0"


def test_sphere_repr():
    test_sphere = Sphere(5)
    assert repr(test_sphere) == "Sphere(5.0)"


def test_sphere_addition():
    test_sphere_1 = Sphere(2)
    test_sphere_2 = Sphere(10)
    assert (test_sphere_1 + test_sphere_2) == Sphere(12)


def test_sphere_subtractions():
    test_sphere_1 = Sphere(12)
    test_sphere_2 = Sphere(10)
    assert (test_sphere_1 - test_sphere_2) == Sphere(2)


def test_sphere_multiplication():
    test_sphere_1 = Sphere(4)
    test_sphere_2 = Sphere(5)
    assert (test_sphere_1 * test_sphere_2) == Sphere(20)


def test_sphere_division():
    test_sphere_1 = Sphere(40)
    test_sphere_2 = Sphere(5)
    assert (test_sphere_1 / test_sphere_2) == Sphere(8)


def test_sphere_less_than():
    test_sphere_1 = Sphere(10)
    test_sphere_2 = Sphere(20)
    assert (test_sphere_1 < test_sphere_2) == True


def test_sphere_less_than_equal_to():
    test_sphere_1 = Sphere(10)
    test_sphere_2 = Sphere(20)
    test_sphere_3 = Sphere(20)
    assert test_sphere_1 < test_sphere_2
    assert test_sphere_2 <= test_sphere_3


def test_sphere_equal_to():
    test_sphere_1 = Sphere(10)
    test_sphere_2 = Sphere(10)
    assert test_sphere_1 == test_sphere_2


def test_sphere_greater_than():
    test_sphere_1 = Sphere(20)
    test_sphere_2 = Sphere(10)
    assert (test_sphere_1 > test_sphere_2) == True


def test_sphere_greater_than_equal_to():
    test_sphere_1 = Sphere(30)
    test_sphere_2 = Sphere(20)
    test_sphere_3 = Sphere(20)
    assert test_sphere_1 > test_sphere_2
    assert test_sphere_2 >= test_sphere_3


def test_sphere_not_equal_to():
    test_sphere_1 = Sphere(20)
    test_sphere_2 = Sphere(10)
    assert test_sphere_1 != test_sphere_2


def test_sort_sphere_list():
    list_of_spheres = [Sphere(20), Sphere(2), Sphere(5)]
    list_of_spheres.sort()
    assert list_of_spheres[0] == Sphere(2)
    assert list_of_spheres[1] == Sphere(5)
    assert list_of_spheres[2] == Sphere(20)


def test_sphere_multiply_by_number():
    test_sphere = Sphere(2)
    assert (test_sphere * 5) == Sphere(10)
    assert (5 * test_sphere) == Sphere(10)
    assert (test_sphere * 5) == (5 * test_sphere)

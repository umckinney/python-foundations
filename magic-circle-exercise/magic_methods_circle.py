#!/usr/bin/env python
"""
A set of classes to manage circle creation, comparison, and arithmetic calculations

Requirements:
    xCreate a class named 'Circle' with properties
        x'radius' (class attribute)
        x'diameter' (calculated value)
        x'area' (calculated value)
    xCircle can be instantiated by setting 'radius' or 'diameter'
        Attempting to set 'area' will result in an error
    xEnsure Circle.__str__ and .__repr__ return human-friendly values
    Ensure n instances of Circle can be added or subtracted
    Ensure an instance of Circle can be multiplied by a number
    Enable comparison operators between 2 Circle instances
    Enable sorting of Circle instances in a list
    Ensure reflected numerics work as expected
    Ensure augmented assignment operators work as expected
    Review all magic methods that are relevant and ensure they work as expected
    Create a subclass of Circle for Sphere
        Override __str__ and __repr__ methods as appropriate
        Create a volume property (4/3 pi r^3)
        Override area property to calculate surface area
        Validate Sphere.from_diameter() returns a valid instance of Sphere
"""


class Circle:
    def __init__(self, input, is_diameter=False):
        from math import pi

        if is_diameter:
            self.radius = input / 2
        else:
            self.radius = float(input)
        self._area = pi * (self.radius**2)

    @property
    def area(self):
        return self._area

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius / other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius / other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.radius != other.radius
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius + other)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius - other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius * other)
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.radius / other)
        return NotImplemented

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter, is_diameter=True)

    def diameter(self):
        return self.radius * 2


class Sphere(Circle):
    def __init__(self, input, is_diameter=False):
        Circle.__init__(self, input)
        if is_diameter:
            self.radius = input / 2
        else:
            self.radius = float(input)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter, is_diameter=True)

    def __str__(self):
        return f"Sphere with radius {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    def area(self):
        from math import pi

        return 4 * pi * (self.radius**2)

    def volume(self):
        from math import pi

        return (4 / 3) * pi * (self.radius**3)


if __name__ == "__main__":
    c = Circle(4)
    print(f"c.radius = {c.radius}")

    d = Circle.from_diameter(50)
    print(f"d.radius = {d.radius}")

    e = c + d
    print(f"e = {e}")

    f = c + 2
    print(f"f = {f}")

    g = c * d
    print(f"g = {g}")

    h = c * 10
    print(f"h = {h}")

    i = 10 * c
    print(f"i = {i}")

    print(c == d, " false")
    print(c > d, " false")
    print(c >= d, " false")
    print(c <= d, " true")
    print(c < d, " true")
    print(c != d, " true")

    list_of_circles = [c, d, e, f]
    print(list_of_circles)
    list_of_circles.sort()
    print(list_of_circles)

    print(f"area of circle c = {c.area}")

# polymorphism_demo.py
import math

class Shape:
    """
    Base class representing a generic shape.
    Subclasses should override area().
    """
    def area(self):
        # Signal that subclasses must implement this method
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """
    Rectangle defined by length and width.
    Overrides area() to return length * width.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    """
    Circle defined by radius.
    Overrides area() to return pi * radius^2.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
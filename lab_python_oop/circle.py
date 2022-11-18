from lab_python_oop.figure import Figure
from lab_python_oop.colour import Colour
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, colour):
        self.radius = radius
        self.fc = Colour()
        self.fc.colorproperty = colour

    def area(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.radius,
            self.area()
        )
from lab_python_oop.figure import Figure
from lab_python_oop.colour import Colour


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
        
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.fc = Colour()
        self.fc.colorproperty = colour

    def area(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.area()
        ) 
        
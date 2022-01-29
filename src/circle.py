from math import pi

from src.figure import Figure


class Circle(Figure):
    def __init__(self, a, name='Circle'):
        self.a = a

        super().__init__(name=name, area=self.get_area(), perimeter=self.get_perimeter())

    def get_area(self):
        return round(pi * self.a * self.a, 2)

    def get_perimeter(self):
        return round(pi * self.a * 2, 2)

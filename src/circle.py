from math import pi

from src._figure import _Figure


class Circle(_Figure):
    def __init__(self, radius):
        self._radius = radius

        super().__init__(name='Circle', area=self.get_area(), perimeter=self.get_perimeter())

    @property
    def radius(self):
        return self._radius

    def get_area(self):
        return round(pi * self.radius * self.radius, 2)

    def get_perimeter(self):
        return round(pi * self.radius * 2, 2)

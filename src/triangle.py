from math import sqrt

from src.figure import Figure


class Triangle(Figure):
    def __new__(cls, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            return None
        return super().__new__(cls)

    def __init__(self, a, b, c, name='Triangle'):
        self.a = a
        self.b = b
        self.c = c

        super().__init__(name=name, area=self.get_area(), perimeter=self.get_perimeter())

    def get_area(self):
        semiperimeter = self.get_perimeter()/2
        return round(sqrt(
            semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c)
        ), 2)

    def get_perimeter(self):
        return self.a + self.b + self.c

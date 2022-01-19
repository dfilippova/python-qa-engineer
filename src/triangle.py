from math import sqrt

from src._figure import _Figure


class Triangle(_Figure):
    def __new__(cls, first_edge, second_edge, third_edge):
        if (
            first_edge + second_edge > third_edge and
            first_edge + third_edge > second_edge and
            second_edge + third_edge > first_edge
        ):
            return super().__new__(cls)

    def __init__(self, first_edge, second_edge, third_edge):
        self._first_edge = first_edge
        self._second_edge = second_edge
        self._third_edge = third_edge

        super().__init__(name='Triangle', area=self.get_area(), perimeter=self.get_perimeter())

    @property
    def first_edge(self):
        return self._first_edge

    @property
    def second_edge(self):
        return self._second_edge

    @property
    def third_edge(self):
        return self._third_edge

    def get_area(self):
        semiperimeter = self.get_perimeter()/2
        return round(sqrt(
            semiperimeter * (semiperimeter - self.first_edge) * (semiperimeter - self.second_edge) *
            (semiperimeter - self.third_edge)
        ), 2)

    def get_perimeter(self):
        return self.first_edge + self.second_edge + self.third_edge

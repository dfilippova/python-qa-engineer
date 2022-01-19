from src._figure import _Figure


class Rectangle(_Figure):
    def __init__(self, length, width, name='Rectangle'):
        self._length = length
        self._width = width

        super().__init__(name=name, area=self.get_area(), perimeter=self.get_perimeter())

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2

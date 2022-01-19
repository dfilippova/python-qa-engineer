class _Figure:
    def __init__(self, name, area, perimeter):
        self._name = name
        self._area = area
        self._perimeter = perimeter

    @property
    def name(self):
        return self._name

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    def add_area(self, figure: '_Figure'):
        if not isinstance(figure, _Figure):
            raise ValueError("Передан неправильный класс!")
        return round(self.area + figure.area, 2)

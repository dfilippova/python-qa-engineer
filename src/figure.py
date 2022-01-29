class Figure:
    def __init__(self, name, area, perimeter):
        if self.__class__ == Figure:
            raise Exception('Экземпляр базового класса не может быть создан!')
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, figure: 'Figure'):
        if not isinstance(figure, Figure):
            raise ValueError("Передан неправильный класс!")
        return round(self.area + figure.area, 2)

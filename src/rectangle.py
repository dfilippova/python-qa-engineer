from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name='Rectangle'):
        self.a = a
        self.b = b

        super().__init__(name=name, area=self.get_area(), perimeter=self.get_perimeter())

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2

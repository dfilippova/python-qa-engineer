from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        self._side = side

        super().__init__(length=side, width=side, name='Square')

    @property
    def side(self):
        return self._side

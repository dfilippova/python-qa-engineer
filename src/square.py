from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a, name='Square'):

        super().__init__(a=a, b=a, name=name)

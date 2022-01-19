from src.rectangle import Rectangle


def test_rectangle_creation(default_rectangle):
    """Проверка создания прямоугольника"""
    assert isinstance(default_rectangle, Rectangle)


def test_rectangle_name(default_rectangle):
    """Проверка имени прямоугольника"""
    assert default_rectangle.name == 'Rectangle'


def test_rectangle_area():
    """Проверка вычисления площади прямоугольника"""
    rectangle_length = 2
    rectangle_width = 4
    rectangle_area = 8

    rectangle = Rectangle(rectangle_length, rectangle_width)
    assert rectangle.area == rectangle_area


def test_rectangle_perimeter():
    """Проверка вычисления периметра прямоугольника"""
    rectangle_length = 10
    rectangle_width = 7
    rectangle_perimeter = 34

    rectangle = Rectangle(rectangle_length, rectangle_width)
    assert rectangle.perimeter == rectangle_perimeter

from src.square import Square


def test_square_creation(default_square):
    """Проверка создания круга"""
    assert isinstance(default_square, Square)


def test_square_name(default_square):
    """Проверка имени круга"""
    assert default_square.name == 'Square'


def test_square_area():
    """Проверка вычисления площади квадрата"""
    square_side = 4
    square_area = 16

    square = Square(square_side)
    assert square.area == square_area


def test_square_perimeter():
    """Проверка вычисления периметра квадрата"""
    square_side = 7
    square_perimeter = 28

    square = Square(square_side)
    assert square.perimeter == square_perimeter

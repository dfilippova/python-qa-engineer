from src.circle import Circle


def test_circle_creation(default_circle):
    """Проверка создания круга"""
    assert isinstance(default_circle, Circle)


def test_circle_name(default_circle):
    """Проверка имени круга"""
    assert default_circle.name == 'Circle'


def test_circle_area():
    """Проверка вычисления площади круга"""
    circle_radius = 7
    circle_area = 153.94

    circle = Circle(circle_radius)
    assert circle.area == circle_area


def test_circle_perimeter():
    """Проверка вычисления периметра круга"""
    circle_radius = 5
    circle_perimeter = 31.42

    circle = Circle(circle_radius)
    assert circle.perimeter == circle_perimeter

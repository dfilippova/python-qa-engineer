from src.triangle import Triangle


def test_correct_triangle_creation(default_triangle):
    """Проверка создания правильного треугольника"""
    assert isinstance(default_triangle, Triangle)


def test_incorrect_triangle_creation():
    """Проверка создания неправильного треугольника"""
    triangle = Triangle(3, 50, 6)
    assert not triangle


def test_triangle_name(default_triangle):
    """Проверка имени треугольника"""
    assert default_triangle.name == 'Triangle'


def test_triangle_area():
    """Проверка вычисления площади треугольника"""
    triangle_first_edge = 4
    triangle_second_edge = 7
    triangle_third_edge = 10
    triangle_area = 10.93

    triangle = Triangle(triangle_first_edge, triangle_second_edge, triangle_third_edge)
    assert triangle.area == triangle_area


def test_triangle_perimeter():
    """Проверка вычисления периметра треугольника"""
    triangle_first_edge = 8
    triangle_second_edge = 5
    triangle_third_edge = 7
    triangle_perimeter = 20

    triangle = Triangle(triangle_first_edge, triangle_second_edge, triangle_third_edge)
    assert triangle.perimeter == triangle_perimeter

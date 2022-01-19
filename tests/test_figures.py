import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize('first_figure, second_figure', [
    (Circle(4), Rectangle(2, 6)),
    (Circle(7), Square(3)),
    (Circle(2), Triangle(5, 2, 6)),
    (Rectangle(3, 1), Square(4)),
    (Rectangle(8, 8), Triangle(6, 6, 2)),
    (Square(11), Triangle(3, 3, 3))
], ids=[
    'circle + rectangle',
    'circle + square',
    'circle + triangle',
    'rectangle + square',
    'rectangle + triangle',
    'square + triangle'
])
def test_area_addition(first_figure, second_figure):
    """Проверка добавления площади"""
    assert first_figure.add_area(second_figure) == round(first_figure.area + second_figure.area, 2)


def test_incorrect_area_addition(default_circle):
    """Проверка передачи неправильного класса при добавлении площади"""
    error = 'После передачи неправильного класса должна появляться ошибка ValueError!'

    try:
        default_circle.add_area(5)
    except ValueError:
        error = ''
    assert not error

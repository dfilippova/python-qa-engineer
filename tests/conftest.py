import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def default_circle():
    return Circle(4)


@pytest.fixture
def default_rectangle():
    return Rectangle(3, 6)


@pytest.fixture
def default_square():
    return Square(5)


@pytest.fixture
def default_triangle():
    return Triangle(3, 5, 6)

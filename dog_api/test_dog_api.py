import pytest
import requests
from jsonschema import validate


def test_list_all_breeds(base_url):
    """Проверка получения списка всех пород собак"""
    response = requests.get(f'{base_url}/breeds/list/all')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'object'},
            'status': {'type': 'string'}
        },
        'required': ['message', 'status']
    }
    validate(instance=response.json(), schema=schema)


def test_random_image_from_all_dogs(base_url):
    """Проверка получения случайного изображения из коллекции всех собак"""
    response = requests.get(f'{base_url}/breeds/image/random')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'string'},
            'status': {'type': 'string'}
        },
        'required': ['message', 'status']
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('amount', [0, 1, 25, 50, 51], ids=[
    'min invalid value', 'min valid value', 'average valid value', 'max valid value', 'max invalid value'
])
def test_random_images_from_all_dogs(base_url, amount):
    """Проверка получения нужного количества случайных изображений из коллекции всех собак"""
    correct_amount = amount
    response = requests.get(f'{base_url}/breeds/image/random/{amount}')
    assert response.status_code == 200

    if amount < 1:
        correct_amount = 1
    elif amount > 50:
        correct_amount = 50

    assert len(response.json()['message']) == correct_amount


@pytest.mark.parametrize('breed', ['akita', 'collie', 'spaniel', 'retriever', 'terrier'], ids=[
    'akita', 'collie', 'spaniel', 'retriever', 'terrier'
])
@pytest.mark.parametrize('amount', [0, 1, 5000], ids=[
    'min invalid value', 'min valid value', 'max valid value'
])
def test_random_images_from_breed(base_url, breed, amount):
    """Проверка получения нужного количества случайных изображений из коллекции собак определенной породы"""
    correct_amount = amount
    max_amount = len(requests.get(f'{base_url}/breed/{breed}/images').json()['message'])
    response = requests.get(f'{base_url}/breed/{breed}/images/random/{amount}')
    assert response.status_code == 200

    if amount < 1:
        correct_amount = 1
    if amount > max_amount:
        correct_amount = max_amount

    for image in response.json()['message']:
        assert breed in image

    assert len(response.json()['message']) == correct_amount


def test_list_all_sub_breeds(base_url):
    """Проверка получения массива всех породных групп породы собак"""
    response = requests.get(f'{base_url}/breed/hound/list')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'array'},
            'status': {'type': 'string'}
        },
        'required': ['message', 'status']
    }
    validate(instance=response.json(), schema=schema)

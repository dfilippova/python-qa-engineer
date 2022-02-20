import pytest
import requests
from jsonschema import validate


def test_list_all_breweries(base_url):
    """Проверка получения списка всех пивоварен"""
    response = requests.get(f'{base_url}/breweries')
    assert response.status_code == 200

    schema = {
        'type': 'array',
        'value': {
            'type': 'object'
        }
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('amount', [-1, 0, 1, 25, 50, 51], ids=[
    'min invalid value', 'zero', 'min valid value', 'average valid value', 'max valid value', 'max invalid value'
])
def test_breweries_per_page(base_url, amount):
    """Проверка получения нужного количества пивоварен"""
    correct_amount = amount
    response = requests.get(f'{base_url}/breweries?per_page={amount}')
    assert response.status_code == 200

    if amount < 0:
        correct_amount = 20
    elif amount > 50:
        correct_amount = 50

    assert len(response.json()) == correct_amount


def test_brewery(base_url):
    """Проверка получения конкретной пивоварни"""
    response = requests.get(f'{base_url}/breweries/blind-pig-brewery-champaign')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'name': {'type': 'string'},
            'brewery_type': {'type': 'string'},
            'street': {'type': 'string'},
            'address_2': {'type': 'null'},
            'address_3': {'type': 'null'},
            'city': {'type': 'string'},
            'state': {'type': 'string'},
            'county_province': {'type': 'null'},
            'postal_code': {'type': 'string'},
            'country': {'type': 'string'},
            'longitude': {'type': 'string'},
            'latitude': {'type': 'string'},
            'phone': {'type': 'string'},
            'website_url': {'type': 'string'},
            'updated_at': {'type': 'string'},
            'created_at': {'type': 'string'}
        },
        'required': ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'county_province', 'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url',
                     'updated_at', 'created_at']
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('query', ['dog', 'cat', 'pig'], ids=['dog', 'cat', 'pig'])
@pytest.mark.xfail(reason='Ошибка в API, количество пивоварен должно быть не больше 15')
def test_list_breweries_on_search_term(base_url, query):
    """Проверка получения списка пивоварен по поисковому запросу"""
    response = requests.get(f'{base_url}/breweries/autocomplete?query={query}')
    assert response.status_code == 200

    schema = {
        'type': 'array',
        'value': {
            'type': 'object'
        }
    }
    validate(instance=response.json(), schema=schema)

    for brewery in response.json():
        assert query in brewery['id'] or query in brewery['name']

    assert len(response.json()) <= 15


@pytest.mark.parametrize('city', ['london', 'paris', 'new_york'], ids=['London', 'Paris', 'New York'])
def test_filter_by_city(base_url, city):
    """Проверка фильтрации пивоварен по городу"""
    response = requests.get(f'{base_url}/breweries?by_city={city}')
    assert response.status_code == 200

    city = city.replace('_', ' ')
    for brewery in response.json():
        assert city in brewery['city'].lower()

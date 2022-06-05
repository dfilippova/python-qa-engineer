import requests


def test_url_status_code(url, status_code):
    """Проверка соответствия ссылки и статуса ответа"""
    response = requests.get(url)
    assert response.status_code == status_code

import pytest
import requests


@pytest.mark.parametrize('post_id', [0, 1, 50, 100, 101], ids=[
    'min invalid id', 'min valid id', 'average valid id', 'max valid id', 'max invalid id'
])
def test_get_post_by_id(base_url, post_id):
    """Проверка получения поста по идентификатору"""
    response = requests.get(f'{base_url}/posts/{post_id}')
    if post_id < 1 or post_id > 100:
        assert response.status_code == 404
    else:
        assert response.status_code == 200

    if 1 <= post_id <= 100:
        assert response.json()['id'] == post_id


@pytest.mark.parametrize('elements, amount', [
    ('posts', 100),
    ('comments', 500),
    ('albums', 100),
    ('photos', 5000),
    ('todos', 200),
    ('users', 10)
    ], ids=['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_elements_amount(base_url, elements, amount):
    """Проверка количества элементов (постов, комментариев, альбомов, ...)"""
    response = requests.get(f'{base_url}/{elements}')
    assert response.status_code == 200
    assert len(response.json()) == amount


def test_filter_posts_by_id(base_url):
    """Проверка фильтрации постов по идентификатору пользователя"""
    response = requests.get(f'{base_url}/posts?userId=1')
    assert response.status_code == 200

    for post in response.json():
        assert post['userId'] == 1


def test_create_post(base_url):
    """Проверка создания нового поста"""
    title = 'test post title'
    body = 'test post body'
    user_id = '1'

    response = requests.post('https://jsonplaceholder.typicode.com/posts', data={
        'title': title, 'body': body, 'userId': user_id,
    })
    assert response.status_code == 201

    assert response.json()['id'] == 101
    assert response.json()['title'] == title
    assert response.json()['body'] == body
    assert response.json()['userId'] == user_id


def test_delete_post(base_url):
    """Проверка удаления поста"""
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert response.json() == {}

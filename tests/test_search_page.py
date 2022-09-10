import allure

from page_objects.home_page import HomePage


@allure.feature('Главная страница')
@allure.feature('Страница поиска')
@allure.title('Проверка поиска с главной страницы')
def test_search_on_home_page(driver):
    """
    Кейс:
    - зайти на главную страницу
    - ввести в инпут поиска запрос "mac"
    - нажать на кнопку поиска
    Ожидается:
    - содержимое инпута на странице поиска соответствует поисковому запросу
    -
    """
    data = 'mac'

    home_page = HomePage(driver)

    search_page = home_page.header.search_elements(data)
    data_from_search_input = search_page.get_data_from_search_input()

    assert data_from_search_input == data, (
        f'Содержимое инпута на странице поиска должно соответствовать поисковому запросу - "{data}", '
        f'но фактически соответствует "{data_from_search_input}"'
    )

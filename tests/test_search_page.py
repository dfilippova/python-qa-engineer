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
    - найденные продукты соответствуют поисковому запросу
    """
    data = 'mac'

    home_page = HomePage(driver)

    search_page = home_page.header.search_elements(data)
    data_from_search_input = search_page.get_data_from_search_input()

    with allure.step('Проверить содержимое инпута на странице поиска'):
        if data_from_search_input != data:
            allure.attach(body=search_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(
                f'Содержимое инпута на странице поиска должно соответствовать поисковому запросу - "{data}", '
                f'но фактически соответствует "{data_from_search_input}"'
            )

    with allure.step('Проверить что найденные продукты соответствуют поисковому запросу'):
        for product_name in search_page.get_product_names():
            if data not in product_name.lower():
                raise AssertionError(f'Найденный продукт "{product_name}" не соответствует поисковому запросу "{data}"')

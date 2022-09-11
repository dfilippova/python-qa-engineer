import allure

from page_objects.home_page import HomePage


@allure.feature('Главная страница')
@allure.feature('Страница сравнения')
@allure.title('Проверка добавление товаров для сравнения')
def test_compare_products(driver):
    """
    Кейс:
    - зайти на главную страницу
    - добавить к сравнению товар "iPhone"
    - добавить к сравнению товар "MacBook"
    Ожидается:
    - добавленные товары отображаются на странице сравнения
    """
    first_product_name = 'iPhone'
    second_product_name = 'MacBook'

    home_page = HomePage(driver)

    home_page.add_product_to_compare(first_product_name)
    home_page.wait_for_scroll_animation()

    home_page.add_product_to_compare(second_product_name)
    home_page.wait_for_scroll_animation()

    product_comparison_page = home_page.go_to_product_comparison_page()
    product_names = product_comparison_page.get_product_names()
    with allure.step(
            f'Проверить что товары {first_product_name} и {second_product_name} отображаются на странице сравнения'
    ):
        if first_product_name not in product_names or second_product_name not in product_names:
            allure.attach(body=home_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(
                f'Товары {first_product_name} и {second_product_name} должны отображаться на странице сравнения'
            )

import allure
import pytest

from page_objects.home_page import HomePage


@allure.feature('Главная страница')
@allure.title('Проверка наличия элементов на главной странице')
def test_elements_on_home_page(driver):
    """
    Кейс:
    - зайти на главную страницу
    Ожидается:
    - блок слайд-шоу отображается на странице
    - заголовок Featured отображается на странице
    - карточки товаров отображаются на странице в количестве 4 штук
    - кнопки Add to Cart отображаются на странице в количестве 4 штук
    - блок карусель отображается на странице
    """
    home_page = HomePage(driver)

    # Ожидание появления блока слайд-шоу
    home_page.wait_for_element_to_appear(
        locator=home_page.SLIDESHOW,
        message='Блок слайд-шоу отсутствует на главной странице'
    )

    # Ожидание появления заголовка Featured
    home_page.wait_for_element_to_appear(
        locator=home_page.FEATURED_HEADER,
        message='Заголовок Featured отсутствует на главной странице'
    )

    # Ожидание появления четырех карточек товаров
    home_page.wait_for_elements_to_appear(
        locator=home_page.PRODUCT_CARD,
        message='Количество карточек товаров на главной странице не соответствует четырем',
        quantity=4
    )

    # Ожидание появления четырех кнопок Add to Cart
    home_page.wait_for_elements_to_appear(
        locator=home_page.ADD_TO_CART_BUTTON,
        message='Количество кнопок Add to Cart на главной странице не соответствует четырем',
        quantity=4
    )

    # Ожидание появления блока карусель
    home_page.wait_for_element_to_appear(
        locator=home_page.CAROUSEL,
        message='Блок карусель отсутствует на главной странице'
    )


@allure.feature('Главная страница')
@allure.title('Проверка регистрации нового пользователя')
def test_register_account_on_home_page(driver):
    """
    Кейс:
    - зайти на главную страницу
    - открыть страницу регистрации пользователя с помощью кнопки My account
    - ввести данные пользователя и нажать на кнопку Continue
    Ожидается:
    - выпадающее меню появляется после нажатия на кнопку My account
    - заголовок Your Account Has Been Created! отображается после регистрации пользователя
    """
    home_page = HomePage(driver)

    register_account_page = home_page.header.open_register_account_page()
    success_register_account_page = register_account_page.register_account()
    success_register_account_page.check_success_header()


@allure.feature('Главная страница')
@allure.title('Проверка изменения валюты')
@pytest.mark.parametrize('currency', ['€', '£', '$'], ids=['euro', 'pound sterling', 'us dollar'])
def test_currency_change_on_home_page(driver, currency):
    """
    Кейс:
    - зайти на главную страницу
    - изменить валюту
    Ожидается:
    - выпадающее меню появляется после нажатия на кнопку Currency
    - валюта на кнопке корзины соответствует выбранной
    """
    home_page = HomePage(driver)

    home_page.header.change_currency(currency)
    home_page.header.check_currency_from_cart_button(currency)

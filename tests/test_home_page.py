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
    - открыть страницу регистрации пользователя с помощью кнопки My account и пункта меню Register
    - ввести данные пользователя и нажать на кнопку Continue
    - выйти из аккаунта пользователя с помощью кнопки My account и пункта меню Logout
    Ожидается:
    - выпадающее меню появляется после нажатия на кнопку My account
    - заголовок Your Account Has Been Created! отображается после регистрации пользователя
    - заголовок Account Logout отображается после выхода из аккаунта пользователя
    """
    home_page = HomePage(driver)

    register_account_page = home_page.header.open_register_account_page()
    success_register_account_page = register_account_page.register_account()
    success_register_account_page.check_success_header()

    logout_page = home_page.header.logout()
    logout_page.check_success_header()


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


@allure.feature('Главная страница')
@allure.title('Проверка создания заказа')
def test_create_order_on_home_page(driver):
    """
    Кейс:
    - зайти на главную страницу
    - добавить в корзину товар "iPhone"
    - перейти в корзину
    - оформить заказ
    Ожидается:
    - выпадающее меню появляется после нажатия на кнопку корзины
    - товар с названием "iPhone" находится в корзине
    - в корзине находится только один товар
    - заголовок Your order has been placed! отображается после создания заказа
    """
    product_name = 'iPhone'

    home_page = HomePage(driver)

    home_page.add_product_to_cart(product_name)
    home_page.wait_for_scroll_animation()
    cart_page = home_page.header.view_cart()

    all_product_names = cart_page.get_product_names()
    with allure.step(f'Проверить что в корзине находится только один товар с названием {product_name}'):
        if product_name not in all_product_names:
            allure.attach(body=cart_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(f'Товар с названием {product_name} должен находится в корзине')
        elif len(all_product_names) != 1:
            allure.attach(body=cart_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(f'В корзине должен находиться только один товар')

    checkout_page = cart_page.checkout()
    checkout_page.wait_for_scroll_animation()
    success_order_page = checkout_page.create_order()
    success_order_page.check_success_header()

    home_page.header.logout()


@allure.feature('Главная страница')
@allure.title('Проверка добавление и удаления товара в меню корзины')
def test_remove_product_from_cart_menu_on_home_page(driver):
    """
    Кейс:
    - зайти на главную страницу
    - добавить в корзину товар "iPhone"
    - удалить товар "iPhone" из меню корзины
    Ожидается:
    - товар "iPhone" отображается в выпадающем меню корзины после добавления
    - товар "iPhone" не отображается в выпадающем меню корзины после удаления
    """
    product_name = 'iPhone'

    home_page = HomePage(driver)

    home_page.add_product_to_cart('iPhone')
    home_page.wait_for_scroll_animation()
    with allure.step(f'Проверить что товар {product_name} отображается в меню корзины'):
        if product_name not in home_page.header.get_all_product_names_from_cart_menu():
            allure.attach(body=home_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(f'Товар с названием {product_name} должен отображаться в меню корзины')

    home_page.header.remove_product_from_cart_menu(product_name)
    with allure.step(f'Проверить что товар {product_name} не отображается в меню корзины'):
        if product_name in home_page.header.get_all_product_names_from_cart_menu():
            allure.attach(body=home_page.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(f'Товар с названием {product_name} не должен отображаться в меню корзины')

from page_objects.home_page import HomePage


def test_elements_on_home_page(driver, url):
    """Проверка наличия элементов на главной странице"""
    driver.get(f'{url}:8081')
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
    home_page.wait_for_element_to_appear(
        locator=home_page.PRODUCT_CARD,
        message='Количество карточек товаров на главной странице не соответствует четырем',
        quantity=4
    )

    # Ожидание появления четырех кнопок Add to Cart
    home_page.wait_for_element_to_appear(
        locator=home_page.ADD_TO_CART_BUTTON,
        message='Количество кнопок Add to Cart на главной странице не соответствует четырем',
        quantity=4
    )

    # Ожидание появления блока карусель
    home_page.wait_for_element_to_appear(
        locator=home_page.CAROUSEL,
        message='Блок карусель отсутствует на главной странице'
    )


def test_register_account(driver, url):
    """Проверка регистрации нового пользователя"""
    driver.get(f'{url}:8081')
    home_page = HomePage(driver)

    register_account_page = home_page.header.open_register_account_page()
    success_register_account_page = register_account_page.register_account()
    success_register_account_page.check_success_header()

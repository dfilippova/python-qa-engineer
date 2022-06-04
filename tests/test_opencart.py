from page_objects.catalog_page import CatalogPage
from page_objects.home_page import HomePage
from page_objects.login_admin_page import LoginAdminPage
from page_objects.product_page import ProductPage
from page_objects.register_account_page import RegisterAccountPage


def test_home_page(driver, url):
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


def test_catalog_page(driver, url):
    """Проверка наличия элементов на странице каталога"""
    driver.get(f'{url}:8081/desktops')
    catalog_page = CatalogPage(driver)

    # Ожидание появления блока со списком групп
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.GROUP_LIST,
        message='Блок со списком групп отсутствует на странице каталога'
    )

    # Ожидание появления кнопки List
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.LIST_BUTTON,
        message='Кнопка List отсутствует на странице каталога'
    )

    # Ожидание появления кнопки Grid
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.GRID_BUTTON,
        message='Кнопка Grid отсутствует на странице каталога'
    )

    # Ожидание появления ссылки Product Compare
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.PRODUCT_COMPARE_LINK,
        message='Ссылка Product Compare отсутствует на странице каталога'
    )

    # Ожидание появления двенадцати карточек товаров
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.PRODUCT_CARD,
        message='Количество карточек товаров на странице каталога не соответствует двенадцати',
        quantity=12
    )


def test_product_page(driver, url):
    """Проверка наличия элементов на странице товара"""
    driver.get(f'{url}:8081/iphone')
    product_page = ProductPage(driver)

    # Ожидание появления основного (большого) изображения на странице товара
    product_page.wait_for_element_to_appear(
        locator=product_page.BIG_IMAGE,
        message='Количество больших изображений на странице товара не соответствует одному'
    )

    # Ожидание появления дополнительных (маленьких) изображений на странице товара
    product_page.wait_for_element_to_appear(
        locator=product_page.SMALL_IMAGE,
        message='Количество маленьких изображений на странице товара не соответствует пяти',
        quantity=5
    )

    # Ожидание появления инпута Quantity
    product_page.wait_for_element_to_appear(
        locator=product_page.QUANTITY_INPUT,
        message='Инпут Quantity отсутствует на странице товара'
    )

    # Ожидание появления кнопки Add to Cart
    product_page.wait_for_element_to_appear(
        locator=product_page.ADD_TO_CART_BUTTON,
        message='Кнопка Add to Cart отсутствует на странице товара'
    )

    # Ожидание появления вкладки Description
    product_page.wait_for_element_to_appear(
        locator=product_page.DESCRIPTION_TAB,
        message='Вкладка Description отсутствует на странице товара'
    )

    # Ожидание появления вкладки Review
    product_page.wait_for_element_to_appear(
        locator=product_page.REVIEW_TAB,
        message='Вкладка Review отсутствует на странице товара'
    )


def test_login_admin_page(driver, url):
    """Проверка наличия элементов на странице авторизации админки"""
    driver.get(f'{url}:8081/admin')
    login_admin_page = LoginAdminPage(driver)

    # Ожидание появления логотипа
    login_admin_page.wait_for_element_to_appear(
        locator=login_admin_page.LOGO,
        message='Логотип отсутствует на странице авторизации админки'
    )

    # Ожидание появления инпута Username
    login_admin_page.wait_for_element_to_appear(
        locator=login_admin_page.USERNAME_INPUT,
        message='Инпут Username отсутствует на странице авторизации админки'
    )

    # Ожидание появления инпута Password
    login_admin_page.wait_for_element_to_appear(
        locator=login_admin_page.PASSWORD_INPUT,
        message='Инпут Password отсутствует на странице авторизации админки'
    )

    # Ожидание появления ссылки Forgotten Password
    login_admin_page.wait_for_element_to_appear(
        locator=login_admin_page.FORGOTTEN_PASSWORD_LINK,
        message='Ссылка Forgotten Password отсутствует на странице авторизации админки'
    )

    # Ожидание появления кнопки Login
    login_admin_page.wait_for_element_to_appear(
        locator=login_admin_page.LOGIN_BUTTON,
        message='Кнопка Login отсутствует на странице авторизации админки'
    )


def test_register_account_page(driver, url):
    """Проверка наличия элементов на странице регистрации пользователя"""
    driver.get(f'{url}:8081/index.php?route=account/register')
    register_account_page = RegisterAccountPage(driver)

    # Ожидание появления ссылки на страницу авторизации
    register_account_page.wait_for_element_to_appear(
        locator=register_account_page.LOGIN_PAGE_LINK,
        message='Ссылка на страницу авторизации отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления блока со списком групп
    register_account_page.wait_for_element_to_appear(
        locator=register_account_page.GROUP_LIST,
        message='Блок со списком групп отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления инпута First Name
    register_account_page.wait_for_element_to_appear(
        locator=register_account_page.FIRST_NAME_INPUT,
        message='Инпут First Name отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления чекбокса Privacy Policy
    register_account_page.wait_for_element_to_appear(
        locator=register_account_page.PRIVACY_POLICY_CHECKBOX,
        message='Чекбокс Privacy Policy отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления кнопки Continue
    register_account_page.wait_for_element_to_appear(
        locator=register_account_page.CONTINUE_BUTTON,
        message='Кнопка Continue отсутствует на странице регистрации пользователя'
    )

import allure

from page_objects.admin_page import AdminPage


@allure.feature('Страница админки')
@allure.title('Проверка наличия элементов на странице авторизации админки')
def test_elements_on_admin_page(driver, url):
    """
    Кейс:
    - зайти на страницу админки /admin
    Ожидается:
    - логотип отображается на странице
    - инпут Username отображается на странице
    - инпут Password отображается на странице
    - ссылка Forgotten Password отображается на странице
    - кнопка Login отображается на странице
    """
    driver.get(f'{url}:8081/admin')
    login_admin_page = AdminPage(driver)

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


@allure.feature('Страница админки')
@allure.title('Проверка добавления нового товара в админке')
def test_add_product_on_admin_page(driver, url):
    """
    Кейс:
    - зайти на страницу админки /admin
    - авторизоваться под админом
    - перейти в раздел товаров
    - ввести данные товара и нажать на кнопку
    Ожидается:
    - добавленный товар отображается в таблице товаров
    """
    product_name = 'New product'

    driver.get(f'{url}:8081/admin')
    admin_page = AdminPage(driver)
    admin_page.login()

    admin_page.go_to_products_section()
    admin_page.add_product(product_name)
    admin_page.check_product_name_in_product_table(product_name)


@allure.feature('Страница админки')
@allure.title('Проверка удаления товара в админке')
def test_delete_product_on_admin_page(driver, url):
    """
    Кейс:
    - зайти на страницу админки /admin
    - авторизоваться под администратором
    - перейти в раздел товаров
    - найти нужный товар и удалить его
    Ожидается:
    - выбранный товар не отображается в таблице товаров
    """
    product_name = 'New product'

    driver.get(f'{url}:8081/admin')
    admin_page = AdminPage(driver)
    admin_page.login()

    admin_page.go_to_products_section()
    admin_page.delete_product(product_name)
    admin_page.check_product_name_not_in_product_table(product_name)

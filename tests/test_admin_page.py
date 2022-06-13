from page_objects.admin_page import AdminPage


def test_elements_on_admin_page(driver, url):
    """Проверка наличия элементов на странице авторизации админки"""
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


def test_add_product_on_admin_page(driver, url):
    """Проверка добавления нового товара в админке"""
    product_name = 'New product'

    driver.get(f'{url}:8081/admin')
    admin_page = AdminPage(driver)
    admin_page.login()

    admin_page.go_to_products_section()
    admin_page.add_product(product_name)
    admin_page.check_product_name_in_product_table(product_name)


def test_delete_product_on_admin_page(driver, url):
    """Проверка удаления товара в админке"""
    product_name = 'New product'

    driver.get(f'{url}:8081/admin')
    admin_page = AdminPage(driver)
    admin_page.login()

    admin_page.go_to_products_section()
    admin_page.delete_product(product_name)
    admin_page.check_product_name_not_in_product_table(product_name)

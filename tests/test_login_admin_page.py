from page_objects.login_admin_page import LoginAdminPage


def test_elements_on_login_admin_page(driver, url):
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

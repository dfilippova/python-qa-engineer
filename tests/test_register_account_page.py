import allure

from page_objects.register_account_page import RegisterAccountPage


@allure.feature('Страница регистрации пользователя')
@allure.title('Проверка наличия элементов на странице регистрации пользователя')
def test_elements_on_register_account_page(driver):
    """
    Кейс:
    - зайти на страницу регистрации пользователя
    Ожидается:
    - ссылка на страницу авторизации отображается на странице
    - блок со списком групп отображается на странице
    - инпут First Name отображается на странице
    - чекбокс Privacy Policy отображается на странице
    - кнопка Continue отображается на странице
    """
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

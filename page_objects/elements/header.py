import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.logout_account_page import LogoutAccountPage
from page_objects.register_account_page import RegisterAccountPage


class Header(BasePage):
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[title="My Account"]')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '[id="top"] [class="dropdown-menu"]')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, '[id="form-currency"]')

    @staticmethod
    def get_context_menu_item(item_name: str):
        return By.XPATH, f'//*[contains(@class, "dropdown-menu")]//*[contains(text(), "{item_name}")]'

    @staticmethod
    def get_currency_from_currency_button(currency: str):
        return By.XPATH, f'//*[@id="form-currency"]//*[@data-toggle="dropdown"]//*[contains(text(), "{currency}")]'

    @staticmethod
    def get_currency_from_cart_button(currency: str):
        return By.XPATH, f'//*[contains(@id, "cart-total")][contains(text(), "{currency}")]'

    @allure.step('Открыть страницу регистрации пользователя с помощью кнопки My account')
    def open_register_account_page(self) -> RegisterAccountPage:
        self.click_on_element(self.MY_ACCOUNT_BUTTON)
        self.wait_for_element_to_appear(
            locator=self.DROPDOWN_MENU,
            message='Меню не появилось после нажатия на кнопку'
        )

        self.click_on_element(self.get_context_menu_item('Register'))
        return RegisterAccountPage(self.driver)

    def wait_for_currency_change(self, currency: str):
        with allure.step(f'Подождать изменения валюты на {currency} на кнопку Currency'):
            return self.wait_for_element_to_appear(
                locator=self.get_currency_from_currency_button(currency),
                message=f'Валюта не была изменена на {currency}'
            )

    def change_currency(self, currency: str):
        with allure.step(f'Изменить валюту на {currency}'):
            self.click_on_element(self.CURRENCY_BUTTON)
            self.wait_for_element_to_appear(
                locator=self.DROPDOWN_MENU,
                message='Меню не появилось после нажатия на кнопку'
            )

        self.click_on_element(self.get_context_menu_item(currency))
        return self.wait_for_currency_change(currency)

    def check_currency_from_cart_button(self, currency: str):
        with allure.step(f'Проверить что валюта на кнопке корзины изменена на {currency}'):
            return self.wait_for_element_to_appear(
                locator=self.get_currency_from_cart_button(currency),
                message=f'Валюта в кнопке корзины не соответствует {currency}'
            )

    @allure.step('Выйти из аккаунта')
    def logout(self) -> LogoutAccountPage:
        self.click_on_element(self.MY_ACCOUNT_BUTTON)
        self.wait_for_element_to_appear(
            locator=self.DROPDOWN_MENU,
            message='Меню не появилось после нажатия на кнопку'
        )

        self.click_on_element(self.get_context_menu_item('Logout'))
        return LogoutAccountPage(self.driver)

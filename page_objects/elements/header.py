from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
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

    def open_register_account_page(self) -> RegisterAccountPage:
        self.driver.find_element(*self.MY_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_appear(
            locator=self.DROPDOWN_MENU,
            message='Меню не появилось после нажатия на кнопку'
        )

        self.driver.find_element(*self.get_context_menu_item('Register')).click()
        return RegisterAccountPage(self.driver)

    def wait_for_currency_change(self, currency: str):
        return self.wait_for_element_to_appear(
            locator=self.get_currency_from_currency_button(currency),
            message=f'Валюта не была изменена на {currency}'
        )

    def change_currency(self, currency: str):
        self.driver.find_element(*self.CURRENCY_BUTTON).click()
        self.wait_for_element_to_appear(
            locator=self.DROPDOWN_MENU,
            message='Меню не появилось после нажатия на кнопку'
        )

        self.driver.find_element(*self.get_context_menu_item(currency)).click()
        return self.wait_for_currency_change(currency)

    def check_currency_from_cart_button(self, currency: str):
        return self.wait_for_element_to_appear(
            locator=self.get_currency_from_cart_button(currency),
            message=f'Валюта в кнопке корзины не соответствует {currency}'
        )

from typing import List

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.cart_page import CartPage
from page_objects.logout_account_page import LogoutAccountPage
from page_objects.register_account_page import RegisterAccountPage
from page_objects.search_page import SearchPage


class Header(BasePage):
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[title="My Account"]')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '[id="top"] [class="dropdown-menu"]')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, '[id="form-currency"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[id="search"] input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[id="search"] button')
    CART_BUTTON = (By.CSS_SELECTOR, '[id="cart"]')
    CART_MENU = (By.CSS_SELECTOR, '[id="cart"][class*="btn-group btn-block open"] [class*="dropdown-menu pull-right"]')
    VIEW_CART_BUTTON = (
        By.XPATH, '//*[@id="cart"][contains(@class, "btn-group btn-block open")]'
        '//*[contains(@class,"dropdown-menu pull-right")]//*[text()=" View Cart"]'
    )
    CHECKOUT_BUTTON = (
        By.XPATH, '//*[@id="cart"][contains(@class, "btn-group btn-block open")]'
        '//*[contains(@class,"dropdown-menu pull-right")]//*[text()=" Checkout"]'
    )
    PRODUCT_NAME_FROM_CART_MENU = (By.CSS_SELECTOR, '[class*="dropdown-menu pull-right"] [class="text-left"] a')
    TEXT_ON_CART_BUTTON = (By.CSS_SELECTOR, '[id="cart-total"]')

    @staticmethod
    def get_context_menu_item(item_name: str):
        return By.XPATH, f'//*[contains(@class, "dropdown-menu")]//*[contains(text(), "{item_name}")]'

    @staticmethod
    def get_currency_from_currency_button(currency: str):
        return By.XPATH, f'//*[@id="form-currency"]//*[@data-toggle="dropdown"]//*[contains(text(), "{currency}")]'

    @staticmethod
    def get_currency_from_cart_button(currency: str):
        return By.XPATH, f'//*[contains(@id, "cart-total")][contains(text(), "{currency}")]'

    @staticmethod
    def get_remove_button_from_cart_menu(product_name: str):
        return (
            By.XPATH, f'//*[text()="{product_name}"]//parent::*[contains(@class, "text-left")]'
            '//following-sibling::*[contains(@class, "text-center")]//*[@type="button"]'
        )

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

    def search_elements(self, data: str) -> SearchPage:
        with allure.step(f'Найти элементы по тексту "{data}"'):
            self.enter_data(self.SEARCH_INPUT, data)
            self.click_on_element(self.SEARCH_BUTTON)
        return SearchPage(self.driver)

    @allure.step('Открыть меню корзины')
    def open_cart_menu(self):
        if not self.element_is_displayed(self.CART_MENU, timeout=1):
            self.click_on_element(self.CART_BUTTON)
            self.wait_for_element_to_appear(
                locator=self.CART_MENU,
                message='Меню корзины не появилось после нажатия на кнопку'
            )

    @allure.step('Перейти в корзину')
    def view_cart(self) -> CartPage:
        self.open_cart_menu()
        self.click_on_element(self.VIEW_CART_BUTTON)
        return CartPage(self.driver)

    def remove_product_from_cart_menu(self, product_name: str):
        with allure.step(f'Удалить товар {product_name} из меню корзины'):
            self.open_cart_menu()
            self.click_on_element(self.get_remove_button_from_cart_menu(product_name))

    @allure.step('Получить названия товаров из меню корзины')
    def get_all_product_names_from_cart_menu(self) -> List[str]:
        self.logger.info('Получение названий товаров из меню корзины')
        self.open_cart_menu()
        return [
            product.get_attribute('textContent') for product in self.driver.find_elements(
                *self.PRODUCT_NAME_FROM_CART_MENU
            )
        ]

    def check_quantity_and_price_on_cart_button(self, quantity: str = '1', price: str = '0.00'):
        with allure.step(
                f'Проверить что количество товаров на кнопке корзины соответствует {quantity}, а цена составляет {price}'
        ):
            self.logger.info('Проверка количества товаров и цены на кнопке корзины')
            text_on_cart_button = self.driver.find_element(*self.TEXT_ON_CART_BUTTON).get_attribute('textContent')

            if text_on_cart_button[1] != quantity:
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(
                    f'Количество товаров на кнопке корзины не соответствует {quantity}')

            if text_on_cart_button.split('$')[1] != price:
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(
                    f'Цена на кнопке корзины не соответствует {price}')

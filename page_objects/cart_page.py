from typing import List

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.checkout_page import CheckoutPage


class CartPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, '[id="checkout-cart"] [class="table-responsive"] [class="text-left"] a')
    CHECKOUT_BUTTON = (By.XPATH, '//*[contains(@class, "btn btn-primary")][text()="Checkout"]')

    @allure.step('Получить названия товаров в корзине')
    def get_product_names(self) -> List[str]:
        self.logger.info('Получение названий товаров в корзине')
        return [product.get_attribute('textContent') for product in self.driver.find_elements(*self.PRODUCT_NAME)]

    @allure.step('Перейти к оформлению заказа')
    def checkout(self) -> CheckoutPage:
        self.click_on_element(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

from typing import List

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '[id="input-search"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="product-thumb"] [class="caption"] a')

    @allure.step('Получить данные из инпута поиска')
    def get_data_from_search_input(self) -> str:
        self.logger.info('Получение данных из инпута поиска')
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    @allure.step('Получить названия найденных товаров')
    def get_product_names(self) -> List[str]:
        self.logger.info('Получение названий найденных товаров')
        return [product.get_attribute('textContent') for product in self.driver.find_elements(*self.PRODUCT_NAME)]

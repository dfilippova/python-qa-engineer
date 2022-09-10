from typing import List

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '[id="input-search"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="product-thumb"] [class="caption"] a')
    UNSUCCESS_SEARCH_HEADER = (
        By.XPATH, '//*[@id="product-search"]//*[text()="There is no product that matches the search criteria."]'
    )

    @allure.step('Получить данные из инпута поиска')
    def get_data_from_search_input(self) -> str:
        self.logger.info('Получение данных из инпута поиска')
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    @allure.step('Получить названия найденных товаров')
    def get_product_names(self) -> List[str]:
        self.logger.info('Получение названий найденных товаров')
        return [product.get_attribute('textContent') for product in self.driver.find_elements(*self.PRODUCT_NAME)]

    def check_unsuccess_search_header(self):
        self.wait_for_element_to_appear(
            locator=self.UNSUCCESS_SEARCH_HEADER,
            message='Заголовок There is no product that matches the search criteria. должен отображаться на странице'
        )

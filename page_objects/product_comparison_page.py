from typing import List

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductComparisonPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, '[id="product-compare"] a strong')

    @allure.step('Получить названия товаров для сравнения')
    def get_product_names(self) -> List[str]:
        self.logger.info('Получение названий товаров для сравнения')
        return [product.get_attribute('textContent') for product in self.driver.find_elements(*self.PRODUCT_NAME)]

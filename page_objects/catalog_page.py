from typing import List

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{self.url}/desktops')

    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    LIST_BUTTON = (By.CSS_SELECTOR, '[id="list-view"]')
    GRID_BUTTON = (By.CSS_SELECTOR, '[id="grid-view"]')
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, '[id="compare-total"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb"]')
    SORT_INPUT = (By.CSS_SELECTOR, '[id="input-sort"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[id="product-category"] [class="product-thumb"] [class="caption"] a')

    def change_sorting(self, sort_by: str):
        with allure.step(f'Выбрать пункт {sort_by} в дропдауне Sort By'):
            self.logger.info(f'Выбор пункта "{sort_by}" в дропдауне Sort By')
            select = Select(self.driver.find_element(*self.SORT_INPUT))
            select.select_by_visible_text(sort_by)

    @allure.step('Получить список товаров')
    def get_product_list(self) -> List[str]:
        return [product.get_attribute('textContent') for product in self.driver.find_elements(*self.PRODUCT_NAME)]

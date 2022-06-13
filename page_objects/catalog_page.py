from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    LIST_BUTTON = (By.CSS_SELECTOR, '[id="list-view"]')
    GRID_BUTTON = (By.CSS_SELECTOR, '[id="grid-view"]')
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, '[id="compare-total"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb"]')

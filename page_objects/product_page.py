from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    BIG_IMAGE = (By.XPATH, '(//*[contains(@class, "thumbnails")]//*[contains(@class, "thumbnail")])[1]')
    SMALL_IMAGE = (By.CSS_SELECTOR, '[class="image-additional"] [class="thumbnail"]')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '[id="input-quantity"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id="button-cart"]')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '[href="#tab-description"]')
    REVIEW_TAB = (By.CSS_SELECTOR, '[href="#tab-review"]')

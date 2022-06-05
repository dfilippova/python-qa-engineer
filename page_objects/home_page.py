from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.elements.header import Header


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)

    SLIDESHOW = (By.CSS_SELECTOR, '[class="slideshow swiper-viewport"]')
    FEATURED_HEADER = (By.XPATH, '//*[text()="Featured"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb transition"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[text()="Add to Cart"]//parent::*[@type="button"]')
    CAROUSEL = (By.CSS_SELECTOR, '[class="carousel swiper-viewport"]')

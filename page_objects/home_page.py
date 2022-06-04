from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    SLIDESHOW = (By.CSS_SELECTOR, '[class="slideshow swiper-viewport"]')
    FEATURED_HEADER = (By.XPATH, '//*[text()="Featured"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb transition"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[text()="Add to Cart"]//parent::*[@type="button"]')
    CAROUSEL = (By.CSS_SELECTOR, '[class="carousel swiper-viewport"]')

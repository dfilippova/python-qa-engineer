import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.elements.header import Header


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)
        self.driver.get(self.url)

    SLIDESHOW = (By.CSS_SELECTOR, '[class="slideshow swiper-viewport"]')
    FEATURED_HEADER = (By.XPATH, '//*[text()="Featured"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb transition"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[text()="Add to Cart"]//parent::*[@type="button"]')
    CAROUSEL = (By.CSS_SELECTOR, '[class="carousel swiper-viewport"]')

    @staticmethod
    def get_add_to_cart_button(product_name: str):
        return (
            By.XPATH, f'//*[text()="{product_name}"]//ancestor::*[contains(@class, "product-thumb transition")]'
            '//*[@type="button"][1]'
        )

    def add_product_to_cart(self, product_name: str):
        with allure.step(f'Добавить товар {product_name} в корзину'):
            try:
                self.click_on_element(self.get_add_to_cart_button(product_name))
            except NoSuchElementException as e:
                self.logger.error(f'Товар {product_name} не найден')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

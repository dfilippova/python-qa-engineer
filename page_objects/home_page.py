import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.elements.footer import Footer
from page_objects.elements.header import Header
from page_objects.product_comparison_page import ProductComparisonPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)
        self.footer = Footer(self.driver)
        self.driver.get(self.url)

    SLIDESHOW = (By.CSS_SELECTOR, '[class="slideshow swiper-viewport"]')
    FEATURED_HEADER = (By.XPATH, '//*[text()="Featured"]')
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class="product-thumb transition"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[text()="Add to Cart"]//parent::*[@type="button"]')
    CAROUSEL = (By.CSS_SELECTOR, '[class="carousel swiper-viewport"]')
    PRODUCT_COMPARISON_LINK = (
        By.XPATH, '//*[contains(@class, "alert-success")]//*[text()="product comparison"]'
    )

    @staticmethod
    def get_add_to_cart_button(product_name: str):
        return (
            By.XPATH, f'//*[text()="{product_name}"]//ancestor::*[contains(@class, "product-thumb transition")]'
            '//*[@type="button"][1]'
        )

    @staticmethod
    def get_add_to_wishlist_button(product_name: str):
        return (
            By.XPATH, f'//*[text()="{product_name}"]//ancestor::*[contains(@class, "product-thumb transition")]'
            '//*[@type="button"][@data-original-title="Add to Wish List"]'
        )

    @staticmethod
    def get_add_to_compare_button(product_name: str):
        return (
            By.XPATH, f'//*[text()="{product_name}"]//ancestor::*[contains(@class, "product-thumb transition")]'
            '//*[@type="button"][@data-original-title="Compare this Product"]'
        )

    def add_product_to_cart(self, product_name: str):
        with allure.step(f'Добавить товар {product_name} в корзину'):
            try:
                self.click_on_element(self.get_add_to_cart_button(product_name))
            except NoSuchElementException as e:
                self.logger.error(f'Товар {product_name} не найден')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def add_product_to_wishlist(self, product_name: str):
        with allure.step(f'Добавить товар {product_name} в список избранного'):
            try:
                self.click_on_element(self.get_add_to_wishlist_button(product_name))
            except NoSuchElementException as e:
                self.logger.error(f'Товар {product_name} не найден')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def add_product_to_compare(self, product_name: str):
        with allure.step(f'Добавить товар {product_name} в список сравнения'):
            try:
                self.click_on_element(self.get_add_to_compare_button(product_name))
            except NoSuchElementException as e:
                self.logger.error(f'Товар {product_name} не найден')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    @allure.step('Перейти на страницу сравнения')
    def go_to_product_comparison_page(self) -> ProductComparisonPage:
        try:
            self.click_on_element(self.PRODUCT_COMPARISON_LINK)
            return ProductComparisonPage(self.driver)
        except NoSuchElementException as e:
            self.logger.error('Ссылка для перехода на страницу сравнения не найдена')
            allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
            raise AssertionError(e.msg)

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.elements.header import Header


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{self.url}/iphone')
        self.header = Header(self.driver)

    BIG_IMAGE = (By.XPATH, '(//*[contains(@class, "thumbnails")]//*[contains(@class, "thumbnail")])[1]')
    SMALL_IMAGE = (By.CSS_SELECTOR, '[class="image-additional"] [class="thumbnail"]')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '[id="input-quantity"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id="button-cart"]')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '[href="#tab-description"]')
    REVIEW_TAB = (By.CSS_SELECTOR, '[href="#tab-review"]')
    PRICE = (By.CSS_SELECTOR, '[id="product-product"] [class*="list-unstyled"] h2')

    def add_product_to_cart(self, quantity: str = '1'):
        with allure.step(f'Добавить в корзину товар в количестве {quantity}'):
            self.logger.info(f'Добавление в корзину товара в количестве {quantity}')
            self.click_on_element(self.QUANTITY_INPUT)
            ActionChains(self.driver).send_keys(Keys.BACKSPACE).perform()
            self.enter_data(self.QUANTITY_INPUT, quantity)
            self.click_on_element(self.ADD_TO_CART_BUTTON)

    @allure.step('Получить цену товара')
    def get_product_price(self) -> str:
        return self.driver.find_element(*self.PRICE).get_attribute('textContent')

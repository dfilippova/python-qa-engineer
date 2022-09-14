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
    NAME_INPUT = (By.CSS_SELECTOR, '[id="input-name"]')
    REVIEW_INPUT = (By.CSS_SELECTOR, '[id="input-review"]')
    CONTINUE_REVIEW_BUTTON = (By.CSS_SELECTOR, '[id="button-review"]')
    SUCCESS_REVIEW_ALERT = (By.CSS_SELECTOR, '[id="form-review"] [class*="alert-success"]')

    @staticmethod
    def get_rating_radio(rating: str):
        return By.CSS_SELECTOR, f'[name="rating"][value="{rating}"]'

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

    def write_review(self, name: str, review: str, rating: str):
        with allure.step(f'Написать отзыв с именем {name}, текстом {review} и оценкой {rating}'):
            self.logger.info('Добавление отзыва')
            self.click_on_element(self.REVIEW_TAB)

            self.enter_data(self.NAME_INPUT, name)
            self.enter_data(self.REVIEW_INPUT, review)
            self.click_on_element(self.get_rating_radio(rating))

            self.click_on_element(self.CONTINUE_REVIEW_BUTTON)

    def check_success_review_alert(self):
        self.wait_for_element_to_appear(
            locator=self.SUCCESS_REVIEW_ALERT,
            message=(
                'Алерт Thank you for your review. It has been submitted to the webmaster for approval. '
                'должен отображаться на странице'
            )
        )

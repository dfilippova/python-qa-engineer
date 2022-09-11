from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SuccessOrderPage(BasePage):
    SUCCESS_ORDER_HEADER = (By.XPATH, '//*[@id="common-success"]//*[text()="Your order has been placed!"]')

    def check_success_header(self):
        self.wait_for_element_to_appear(
            locator=self.SUCCESS_ORDER_HEADER,
            message='Заголовок Your order has been placed! должен отображаться на странице'
        )

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SuccessRegisterAccountPage(BasePage):
    SUCCESS_REGISTER_ACCOUNT_HEADER = (By.XPATH, '//*[@id="content"]//*[text()="Your Account Has Been Created!"]')

    def check_success_header(self):
        self.wait_for_element_to_appear(
            locator=self.SUCCESS_REGISTER_ACCOUNT_HEADER,
            message='Заголовок Your Account Has Been Created! должен отображаться на странице'
        )

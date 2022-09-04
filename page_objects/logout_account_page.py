from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LogoutAccountPage(BasePage):
    SUCCESS_LOGOUT_HEADER = (By.XPATH, '//*[@id="content"]//*[text()="Account Logout"]')

    def check_success_header(self):
        self.wait_for_element_to_appear(
            locator=self.SUCCESS_LOGOUT_HEADER,
            message='Заголовок Account Logout должен отображаться на странице'
        )

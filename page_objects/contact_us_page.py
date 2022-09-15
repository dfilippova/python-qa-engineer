import allure
from selenium.webdriver.common.by import By

from fake_user import fake_name, fake_email
from page_objects.base_page import BasePage


class ContactUsPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, '[id="information-contact"] [id="input-name"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[id="information-contact"] [id="input-email"]')
    ENQUIRY_INPUT = (By.CSS_SELECTOR, '[id="information-contact"] [id="input-enquiry"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[id="information-contact"] [type="submit"]')
    SUCCESS_ENQUIRY_SENDING_HEADER = (
        By.XPATH, '//*[@id="common-success"]//*[text()="Your enquiry has been successfully sent to the store owner!"]'
    )

    def send_enquiry(self, name: str = fake_name(), email: str = fake_email(), enquiry: str = 'Test enquiry'):
        with allure.step('Отправить запрос с помощью формы Contact Us'):
            self.enter_data(self.NAME_INPUT, name)
            self.enter_data(self.EMAIL_INPUT, email)
            self.enter_data(self.ENQUIRY_INPUT, enquiry)

            self.click_on_element(self.SUBMIT_BUTTON)

    def check_success_enquiry_sending(self):
        self.wait_for_element_to_appear(
            locator=self.SUCCESS_ENQUIRY_SENDING_HEADER,
            message=(
                'Заголовок Your enquiry has been successfully sent to the store owner! должен отображаться на странице'
            )
        )

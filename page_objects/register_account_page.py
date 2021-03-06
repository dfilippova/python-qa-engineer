import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from fake_user import fake_name, fake_last_name, fake_email, fake_phone, fake_password
from page_objects.success_register_account_page import SuccessRegisterAccountPage


class RegisterAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{self.url}/index.php?route=account/register')

    LOGIN_PAGE_LINK = (By.XPATH, '//*[text()="login page"]')
    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[id="input-firstname"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[id="input-lastname"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[id="input-email"]')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '[id="input-telephone"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '[id="input-confirm"]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"][name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    @staticmethod
    def get_subscribe_radiobutton(value: bool):
        if value:
            return By.CSS_SELECTOR, '[name="newsletter"][value="1"]'
        else:
            return By.CSS_SELECTOR, '[name="newsletter"][value="0"]'

    @allure.step('Зарегистрировать аккаунт')
    def register_account(
            self, first_name: str = fake_name(), last_name: str = fake_last_name(), email: str = fake_email(),
            phone: str = fake_phone(), password: str = fake_password(), subscribe: bool = False
    ) -> SuccessRegisterAccountPage:
        self.enter_data(self.FIRST_NAME_INPUT, first_name)
        self.enter_data(self.LAST_NAME_INPUT, last_name)
        self.enter_data(self.EMAIL_INPUT, email)
        self.enter_data(self.TELEPHONE_INPUT, phone)
        self.enter_data(self.PASSWORD_INPUT, password)
        self.enter_data(self.PASSWORD_CONFIRM_INPUT, password)

        self.click_on_element(self.get_subscribe_radiobutton(subscribe))
        self.click_on_element(self.PRIVACY_POLICY_CHECKBOX)
        self.click_on_element(self.CONTINUE_BUTTON)

        return SuccessRegisterAccountPage(self.driver)

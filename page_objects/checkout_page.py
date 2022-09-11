import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fake_user import (
    fake_name, fake_last_name, fake_email, fake_phone, fake_password, fake_address, fake_city, fake_postcode
)
from page_objects.base_page import BasePage
from page_objects.success_order_page import SuccessOrderPage


class CheckoutPage(BasePage):
    CHECKOUT_OPTIONS_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[id="collapse-checkout-option"] [id="button-account"]')
    ACCOUNT_DETAILS_FIRST_NAME_INPUT = (
        By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-firstname"]'
    )
    ACCOUNT_DETAILS_LAST_NAME_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-lastname"]')
    ACCOUNT_DETAILS_EMAIL_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-email"]')
    ACCOUNT_DETAILS_TELEPHONE_INPUT = (
        By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-telephone"]'
    )
    ACCOUNT_DETAILS_PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-password"]')
    ACCOUNT_DETAILS_PASSWORD_CONFIRM_INPUT = (
        By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-confirm"]'
    )
    ACCOUNT_DETAILS_ADDRESS_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-address-1"]')
    ACCOUNT_DETAILS_CITY_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-city"]')
    ACCOUNT_DETAILS_POSTCODE_INPUT = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="input-payment-postcode"]')
    ACCOUNT_DETAILS_REGION_DROPDOWN = (By.CSS_SELECTOR, '[id="input-payment-zone"]')
    ACCOUNT_DETAILS_PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [name="agree"]')
    ACCOUNT_DETAILS_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[id="collapse-payment-address"] [id="button-register"]')

    DELIVERY_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[id="collapse-shipping-method"] [id="button-shipping-method"]')

    PAYMENT_METHOD_PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[id="collapse-payment-method"] [name="agree"]')
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, '[id="collapse-payment-method"] [id="button-payment-method"]')

    CHECKOUT_CONFIRM_BUTTON = (By.CSS_SELECTOR, '[id="collapse-checkout-confirm"] [id="button-confirm"]')

    def create_order(
            self, first_name: str = fake_name(), last_name: str = fake_last_name(), email: str = fake_email(),
            phone: str = fake_phone(), password: str = fake_password(), address: str = fake_address(),
            city: str = fake_city(), post_code: str = fake_postcode(), region: str = 'Angus'
    ) -> SuccessOrderPage:
        with allure.step('Оформить заказ'):
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(*self.CHECKOUT_OPTIONS_CONTINUE_BUTTON)
            ).perform()
            self.click_on_element(self.CHECKOUT_OPTIONS_CONTINUE_BUTTON)
            self.is_ready(self.ACCOUNT_DETAILS_FIRST_NAME_INPUT)

            self.enter_data(self.ACCOUNT_DETAILS_FIRST_NAME_INPUT, first_name)
            self.enter_data(self.ACCOUNT_DETAILS_LAST_NAME_INPUT, last_name)
            self.enter_data(self.ACCOUNT_DETAILS_EMAIL_INPUT, email)
            self.enter_data(self.ACCOUNT_DETAILS_TELEPHONE_INPUT, phone)
            self.enter_data(self.ACCOUNT_DETAILS_PASSWORD_INPUT, password)
            self.enter_data(self.ACCOUNT_DETAILS_PASSWORD_CONFIRM_INPUT, password)
            self.enter_data(self.ACCOUNT_DETAILS_ADDRESS_INPUT, address)
            self.enter_data(self.ACCOUNT_DETAILS_CITY_INPUT, city)
            self.enter_data(self.ACCOUNT_DETAILS_POSTCODE_INPUT, post_code)

            with allure.step(f'Выбрать пункт {region} в дропдауне Region/State'):
                self.logger.info(f'Выбор пункта "{region}" в дропдауне Region/State')
                select = Select(self.driver.find_element(*self.ACCOUNT_DETAILS_REGION_DROPDOWN))
                select.select_by_visible_text(region)

            self.click_on_element(self.ACCOUNT_DETAILS_PRIVACY_POLICY_CHECKBOX)
            self.click_on_element(self.ACCOUNT_DETAILS_CONTINUE_BUTTON)
            self.is_ready(self.DELIVERY_METHOD_CONTINUE_BUTTON)

            self.click_on_element(self.DELIVERY_METHOD_CONTINUE_BUTTON)
            self.is_ready(self.PAYMENT_METHOD_PRIVACY_POLICY_CHECKBOX)

            self.click_on_element(self.PAYMENT_METHOD_PRIVACY_POLICY_CHECKBOX)
            self.click_on_element(self.PAYMENT_METHOD_CONTINUE_BUTTON)
            self.is_ready(self.CHECKOUT_CONFIRM_BUTTON)

            self.click_on_element(self.CHECKOUT_CONFIRM_BUTTON)
            return SuccessOrderPage(self.driver)

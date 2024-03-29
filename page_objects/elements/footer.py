from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.contact_us_page import ContactUsPage


class Footer(BasePage):
    OPENCART_BUTTON = (By.CSS_SELECTOR, 'footer p a')

    @staticmethod
    def get_footer_button(button_name: str):
        return By.XPATH, f'//footer//*[text()="{button_name}"]'

    def contact_us(self) -> ContactUsPage:
        self.click_on_element(self.get_footer_button('Contact Us'))
        return ContactUsPage(self.driver)

    def go_to_opencart_page(self):
        self.click_on_element(self.OPENCART_BUTTON)

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.register_account_page import RegisterAccountPage


class Header(BasePage):
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[title="My Account"]')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '[id="top"] [class="dropdown-menu"]')

    @staticmethod
    def get_context_menu_item(item_name: str):
        return By.XPATH, f'//*[contains(@class, "dropdown-menu")]//*[text()="{item_name}"]'

    def open_register_account_page(self) -> RegisterAccountPage:
        self.driver.find_element(*self.MY_ACCOUNT_BUTTON).click()
        self.wait_for_element_to_appear(
            locator=self.DROPDOWN_MENU,
            message='Меню не появилось после нажатия на кнопку'
        )

        self.driver.find_element(*self.get_context_menu_item('Register')).click()
        return RegisterAccountPage(self.driver)

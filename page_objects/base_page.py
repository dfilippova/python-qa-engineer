from typing import TYPE_CHECKING

from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: 'WebDriver'):
        self.driver = driver

    def wait_for_element_to_appear(self, locator: tuple, message: str, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(
            lambda _driver: self.driver.find_elements(*locator), message=message
        )

    def wait_for_elements_to_appear(self, locator: tuple, message: str, quantity: int = 1, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(
            lambda _driver: len(self.driver.find_elements(*locator)) == quantity, message=message
        )

    def enter_data(self, input_locator: tuple, data: str):
        active_input = self.driver.find_element(*input_locator)
        active_input.click()
        active_input.send_keys(data)

    def confirm_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        #self.browser.refresh()

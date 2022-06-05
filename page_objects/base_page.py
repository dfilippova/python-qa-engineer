from typing import TYPE_CHECKING

from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: 'WebDriver'):
        self.driver = driver

    def wait_for_element_to_appear(self, locator: tuple, message: str, quantity: int = 1, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(
            lambda _driver: len(self.driver.find_elements(*locator)) == quantity, message=message
        )

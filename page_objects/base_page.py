from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_appear(self, locator: tuple, message: str, quantity: int = 1, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(
            lambda _driver: len(self.driver.find_elements(*locator)) == quantity, message=message
        )

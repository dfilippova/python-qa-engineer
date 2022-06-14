from typing import TYPE_CHECKING

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: 'WebDriver'):
        self.driver = driver

    def wait_for_element_to_appear(self, locator: tuple, message: str, timeout: int = 3):
        with allure.step(f'Подождать появления элемента с локатором {locator}'):
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda _driver: self.driver.find_elements(*locator), message=message
                )
            except TimeoutException as e:
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def wait_for_elements_to_appear(self, locator: tuple, message: str, quantity: int = 1, timeout: int = 3):
        with allure.step(f'Подождать появления элементов с локатором {locator} в количестве {quantity}'):
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda _driver: len(self.driver.find_elements(*locator)) == quantity, message=message
                )
            except TimeoutException as e:
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def enter_data(self, input_locator: tuple, data: str):
        with allure.step(f'Ввести данные "{data}" в инпут с локатором {input_locator}'):
            active_input = self.driver.find_element(*input_locator)
            active_input.click()
            active_input.send_keys(data)

    @allure.step('Подтвердить алерт')
    def confirm_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_on_element(self, locator: tuple):
        with allure.step(f'Кликнуть на элемент с локатором {locator}'):
            self.driver.find_element(*locator).click()

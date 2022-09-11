from time import sleep

import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = driver.url
        self.logger = driver.logger

    def wait_for_element_to_appear(self, locator: tuple, message: str, timeout: int = 5):
        with allure.step(f'Подождать появления элемента с локатором {locator}'):
            self.logger.info(f'Ожидание появления элемента с локатором {locator}')
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda _driver: self.driver.find_elements(*locator), message=message
                )
            except TimeoutException as e:
                self.logger.error(f'Элемент с локатором {locator} не появился')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def wait_for_elements_to_appear(self, locator: tuple, message: str, quantity: int = 1, timeout: int = 5):
        with allure.step(f'Подождать появления элементов с локатором {locator} в количестве {quantity}'):
            self.logger.info(f'Ожидание появления элементов с локатором {locator} в количестве {quantity}')
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda _driver: len(self.driver.find_elements(*locator)) == quantity, message=message
                )
            except TimeoutException as e:
                self.logger.error(f'Элементы с локатором {locator} в количестве {quantity} не появились')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    def enter_data(self, input_locator: tuple, data: str):
        with allure.step(f'Ввести данные "{data}" в инпут с локатором {input_locator}'):
            self.logger.info(f'Ввод данных "{data}" в инпут с локатором {input_locator}')
            try:
                active_input = self.driver.find_element(*input_locator)
                active_input.click()
                active_input.send_keys(data)
            except (NoSuchElementException, ElementNotInteractableException) as e:
                self.logger.error(f'Элемент с локатором {input_locator} не найден')
                allure.attach(body=self.driver.get_screenshot_as_png(), name='screenshot')
                raise AssertionError(e.msg)

    @allure.step('Подтвердить алерт')
    def confirm_alert(self):
        self.logger.info('Подтверждение алерта')
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_on_element(self, locator: tuple):
        with allure.step(f'Кликнуть на элемент с локатором {locator}'):
            self.logger.info(f'Клик на элемент с локатором {locator}')
            self.driver.find_element(*locator).click()

    def element_is_displayed(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            return WebDriverWait(self.driver, timeout).until(
                method=lambda _driver: self.driver.find_elements(*locator),
                message=f'Элемент с локатором {locator} не найден'
            )
        except TimeoutException:
            return False

    @allure.step('Подождать окончания анимации')
    def wait_for_scroll_animation(self):
        self.logger.info('Ожидание окончания анимации в течение 1 секунды')
        sleep(1)

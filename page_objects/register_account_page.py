from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class RegisterAccountPage(BasePage):
    LOGIN_PAGE_LINK = (By.XPATH, '//*[text()="login page"]')
    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[id="input-firstname"]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"][name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

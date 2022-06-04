from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginAdminPage(BasePage):
    LOGO = (By.CSS_SELECTOR, '[id="header-logo"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id="input-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    FORGOTTEN_PASSWORD_LINK = (By.XPATH, '//*[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

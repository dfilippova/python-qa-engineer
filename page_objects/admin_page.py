from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOGO = (By.CSS_SELECTOR, '[id="header-logo"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id="input-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    FORGOTTEN_PASSWORD_LINK = (By.XPATH, '//*[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    SUBMENU = (By.CSS_SELECTOR, '[class="collapse in"]')

    PRODUCTS_PAGE_ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCTS_PAGE_PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '[id="filter-product"] [id="input-name"]')
    PRODUCTS_PAGE_FILTER_BUTTON = (By.CSS_SELECTOR, '[id="button-filter"]')

    ADD_PRODUCT_PAGE_PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '[id="input-name1"]')
    ADD_PRODUCT_PAGE_META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, '[id="input-meta-title1"]')
    ADD_PRODUCT_PAGE_MODEL_INPUT = (By.CSS_SELECTOR, '[id="input-model"]')
    ADD_PRODUCT_PAGE_SAVE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    @staticmethod
    def get_item_from_menu(item_name: str):
        return By.XPATH, f'//*[@id="menu"]//*[contains(text(), "{item_name}")]'

    @staticmethod
    def get_tab_from_add_product_form(tab_name: str):
        return By.XPATH, f'//*[@data-toggle="tab"][contains(text(), "{tab_name}")]'

    @staticmethod
    def get_data_from_product_table(item_name: str):
        return By.XPATH, f'//*[@id="form-product"]//*[contains(text(), "{item_name}")]'

    def login(self, username: str = 'user', password: str = 'bitnami'):
        self.enter_data(self.USERNAME_INPUT, username)
        self.enter_data(self.PASSWORD_INPUT, password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def wait_for_submenu_open(self):
        self.wait_for_element_to_appear(
            locator=self.SUBMENU,
            message='Меню не появилось после нажатия на кнопку'
        )

    def add_product(
            self, product_name: str = 'Test product name', meta_tag_title: str = 'Test meta tag title',
            model: str = 'Test model'
    ):
        self.driver.find_element(*self.get_item_from_menu('Catalog')).click()
        self.wait_for_submenu_open()
        self.driver.find_element(*self.get_item_from_menu('Products')).click()

        self.driver.find_element(*self.PRODUCTS_PAGE_ADD_PRODUCT_BUTTON).click()

        self.enter_data(self.ADD_PRODUCT_PAGE_PRODUCT_NAME_INPUT, product_name)
        self.enter_data(self.ADD_PRODUCT_PAGE_META_TAG_TITLE_INPUT, meta_tag_title)

        self.driver.find_element(*self.get_tab_from_add_product_form('Data')).click()
        self.enter_data(self.ADD_PRODUCT_PAGE_MODEL_INPUT, model)

        self.driver.find_element(*self.ADD_PRODUCT_PAGE_SAVE_BUTTON).click()

    def check_product_name_in_product_table(self, product_name: str = 'Test product name'):
        self.enter_data(self.PRODUCTS_PAGE_PRODUCT_NAME_INPUT, product_name)
        self.driver.find_element(*self.PRODUCTS_PAGE_FILTER_BUTTON).click()

        self.wait_for_element_to_appear(
            locator=self.get_data_from_product_table(product_name),
            message=f'Названия {product_name} нет в таблице продуктов'
        )
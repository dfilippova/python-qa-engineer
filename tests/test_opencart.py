from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def test_home_page(driver, url):
    """Проверка наличия элементов на главной странице"""
    driver.get(f'{url}:8081')

    # Ожидание появления блока слайд-шоу
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[class="slideshow swiper-viewport"]'),
        message='Блок слайд-шоу отсутствует на главной странице'
    )

    # Ожидание появления заголовка Featured
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.XPATH, '//*[text()="Featured"]'),
        message='Заголовок Featured отсутствует на главной странице'
    )

    # Ожидание появления четырех карточек товаров
    WebDriverWait(driver, 3).until(
        lambda _driver: len(driver.find_elements(By.CSS_SELECTOR, '[class="product-thumb transition"]')) == 4,
        message='Количество карточек товаров на главной странице не соответствует четырем'
    )

    # Ожидание появления четырех кнопок Add to Cart
    WebDriverWait(driver, 3).until(
        lambda _driver: len(driver.find_elements(
            By.XPATH, '//*[text()="Add to Cart"]//parent::*[@type="button"]'
        )) == 4,
        message='Количество кнопок Add to Cart на главной странице не соответствует четырем'
    )

    # Ожидание появления блока карусель
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[class="carousel swiper-viewport"]'),
        message='Блок карусель отсутствует на главной странице'
    )


def test_catalog_page(driver, url):
    """Проверка наличия элементов на странице каталога"""
    driver.get(f'{url}:8081/desktops')

    # Ожидание появления блока со списком групп
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[class="list-group"]'),
        message='Блок со списком групп отсутствует на странице каталога'
    )

    # Ожидание появления кнопки List
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="list-view"]'),
        message='Кнопка List отсутствует на странице каталога'
    )

    # Ожидание появления кнопки Grid
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="grid-view"]'),
        message='Кнопка Grid отсутствует на странице каталога'
    )

    # Ожидание появления ссылки Product Compare
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="compare-total"]'),
        message='Ссылка Product Compare отсутствует на странице каталога'
    )

    # Ожидание появления двенадцати карточек товаров
    WebDriverWait(driver, 3).until(
        lambda _driver: len(driver.find_elements(By.CSS_SELECTOR, '[class="product-thumb"]')) == 12,
        message='Количество карточек товаров на странице каталога не соответствует двенадцати'
    )


def test_product_page(driver, url):
    """Проверка наличия элементов на странице товара"""
    driver.get(f'{url}:8081/iphone')

    # Ожидание появления основного (большого) изображения на странице товара
    WebDriverWait(driver, 3).until(
        lambda _driver: len(driver.find_elements(
            By.XPATH, '(//*[contains(@class, "thumbnails")]//*[contains(@class, "thumbnail")])[1]'
        )) == 1,
        message='Количество больших изображений на странице товара не соответствует одному'
    )

    # Ожидание появления дополнительных (маленьких) изображений на странице товара
    WebDriverWait(driver, 3).until(
        lambda _driver: len(driver.find_elements(
            By.CSS_SELECTOR, '[class="image-additional"] [class="thumbnail"]'
        )) == 5,
        message='Количество маленьких изображений на странице товара не соответствует пяти'
    )

    # Ожидание появления инпута Quantity
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="input-quantity"]'),
        message='Инпут Quantity отсутствует на странице товара'
    )

    # Ожидание появления кнопки Add to Cart
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="button-cart"]'),
        message='Кнопка Add to Cart отсутствует на странице товара'
    )

    # Ожидание появления вкладки Description
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[href="#tab-description"]'),
        message='Вкладка Description отсутствует на странице товара'
    )

    # Ожидание появления вкладки Review
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[href="#tab-review"]'),
        message='Вкладка Review отсутствует на странице товара'
    )


def test_login_admin_page(driver, url):
    """Проверка наличия элементов на странице авторизации админки"""
    driver.get(f'{url}:8081/admin')

    # Ожидание появления логотипа
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="header-logo"]'),
        message='Логотип отсутствует на странице авторизации админки'
    )

    # Ожидание появления инпута Username
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="input-username"]'),
        message='Инпут Username отсутствует на странице авторизации админки'
    )

    # Ожидание появления инпута Password
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="input-password"]'),
        message='Инпут Password отсутствует на странице авторизации админки'
    )

    # Ожидание появления ссылки Forgotten Password
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.XPATH, '//*[text()="Forgotten Password"]'),
        message='Ссылка Forgotten Password отсутствует на странице авторизации админки'
    )

    # Ожидание появления кнопки Login
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[type="submit"]'),
        message='Кнопка Login отсутствует на странице авторизации админки'
    )


def test_register_account_page(driver, url):
    """Проверка наличия элементов на странице регистрации пользователя"""
    driver.get(f'{url}:8081/index.php?route=account/register')

    # Ожидание появления ссылки на страницу авторизации
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.XPATH, '//*[text()="login page"]'),
        message='Ссылка на страницу авторизации отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления блока со списком групп
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[class="list-group"]'),
        message='Блок со списком групп отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления инпута First Name
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[id="input-firstname"]'),
        message='Инпут First Name отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления чекбокса Privacy Policy
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[type="checkbox"][name="agree"]'),
        message='Чекбокс Privacy Policy отсутствует на странице регистрации пользователя'
    )

    # Ожидание появления кнопки Continue
    WebDriverWait(driver, 3).until(
        lambda _driver: driver.find_element(By.CSS_SELECTOR, '[type="submit"]'),
        message='Кнопка Continue отсутствует на странице регистрации пользователя'
    )

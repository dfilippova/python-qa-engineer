import allure

from page_objects.product_page import ProductPage


@allure.feature('Страница товара')
@allure.title('Проверка наличия элементов на странице товара')
def test_elements_on_product_page(driver, url):
    """
    Кейс:
    - зайти на страницу товара /iphone
    Ожидается:
    - основное изображение отображается на странице
    - дополнительные изображения отображаются на странице в количестве 5 штук
    - инпут Quantity отображается на странице
    - кнопка Add to Cart отображается на странице
    - вкладка Description отображается на странице
    - вкладка Review отображается на странице
    """
    driver.get(f'{url}:8081/iphone')
    product_page = ProductPage(driver)

    # Ожидание появления основного (большого) изображения на странице товара
    product_page.wait_for_element_to_appear(
        locator=product_page.BIG_IMAGE,
        message='Количество больших изображений на странице товара не соответствует одному'
    )

    # Ожидание появления дополнительных (маленьких) изображений на странице товара
    product_page.wait_for_elements_to_appear(
        locator=product_page.SMALL_IMAGE,
        message='Количество маленьких изображений на странице товара не соответствует пяти',
        quantity=5
    )

    # Ожидание появления инпута Quantity
    product_page.wait_for_element_to_appear(
        locator=product_page.QUANTITY_INPUT,
        message='Инпут Quantity отсутствует на странице товара'
    )

    # Ожидание появления кнопки Add to Cart
    product_page.wait_for_element_to_appear(
        locator=product_page.ADD_TO_CART_BUTTON,
        message='Кнопка Add to Cart отсутствует на странице товара'
    )

    # Ожидание появления вкладки Description
    product_page.wait_for_element_to_appear(
        locator=product_page.DESCRIPTION_TAB,
        message='Вкладка Description отсутствует на странице товара'
    )

    # Ожидание появления вкладки Review
    product_page.wait_for_element_to_appear(
        locator=product_page.REVIEW_TAB,
        message='Вкладка Review отсутствует на странице товара'
    )

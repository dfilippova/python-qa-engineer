import allure

from page_objects.catalog_page import CatalogPage


@allure.feature('Страница каталога')
@allure.title('Проверка наличия элементов на странице каталога')
def test_elements_on_catalog_page(driver, url):
    """
    Кейс:
    - зайти на страницу каталога /desktops
    Ожидается:
    - блок со списком групп отображается на странице
    - кнопка List отображается на странице
    - кнопка Grid отображается на странице
    - ссылка Product Compare отображается на странице
    - карточки товаров отображаются на странице в количестве 12 штук
    """
    driver.get(f'{url}:8081/desktops')
    catalog_page = CatalogPage(driver)

    # Ожидание появления блока со списком групп
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.GROUP_LIST,
        message='Блок со списком групп отсутствует на странице каталога'
    )

    # Ожидание появления кнопки List
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.LIST_BUTTON,
        message='Кнопка List отсутствует на странице каталога'
    )

    # Ожидание появления кнопки Grid
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.GRID_BUTTON,
        message='Кнопка Grid отсутствует на странице каталога'
    )

    # Ожидание появления ссылки Product Compare
    catalog_page.wait_for_element_to_appear(
        locator=catalog_page.PRODUCT_COMPARE_LINK,
        message='Ссылка Product Compare отсутствует на странице каталога'
    )

    # Ожидание появления двенадцати карточек товаров
    catalog_page.wait_for_elements_to_appear(
        locator=catalog_page.PRODUCT_CARD,
        message='Количество карточек товаров на странице каталога не соответствует двенадцати',
        quantity=12
    )

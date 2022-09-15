import allure
import pytest

from page_objects.catalog_page import CatalogPage


@allure.feature('Страница каталога')
@allure.title('Проверка наличия элементов на странице каталога')
def test_elements_on_catalog_page(driver):
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


@pytest.mark.parametrize('sort_by, reverse', [('Name (A - Z)', False), ('Name (Z - A)', True)], ids=[
    'Name (A - Z)', 'Name (Z - A)'
])
@allure.feature('Страница каталога')
@allure.title('Проверка сортировки товаров по имени на странице каталога')
def test_sort_elements_on_catalog_page(driver, sort_by, reverse):
    """
    Кейс:
    - зайти на страницу каталога /desktops
    - изменить сортировку
    Ожидается:
    - порядок товаров на странице соответствует сортировке
    """
    catalog_page = CatalogPage(driver)

    product_list = catalog_page.get_product_list()
    product_list.sort(key=str.lower, reverse=reverse)

    catalog_page.change_sorting(sort_by)
    new_product_list = catalog_page.get_product_list()

    if new_product_list != product_list:
        allure.attach(body=catalog_page.driver.get_screenshot_as_png(), name='screenshot')
        raise AssertionError(
            f'Товары на странице должны быть отображены в следующем порядке: {product_list}, '
            f'но фактический порядок: {new_product_list}'
        )

import allure
import pytest

from pages.category_page import CategoryPage
from pages.main_page import MainPage


@allure.story('Проверка, что категория "PC" пустая')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_category_pc_is_empty(browser):
    main_page = MainPage(browser)
    category_page = CategoryPage(browser)

    main_page.open_url()
    main_page.click_on_desktops()
    main_page.click_on_pc()
    category_page.check_pc_is_empty()

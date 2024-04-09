import allure
import pytest

from pages.main_page import MainPage


@allure.story('Поиск')
@allure.title('Проверка поиска')
@pytest.mark.parametrize("browser", ["firefox"], indirect=True)
def test_search(browser):
    main_page = MainPage(browser)
    main_page.open_url()
    main_page.click_on_search()

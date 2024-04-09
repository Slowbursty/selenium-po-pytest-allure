import allure
import pytest

from pages.main_page import MainPage


@allure.story('Проверка смены валюты')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_currency(browser):
    main_page = MainPage(browser)

    main_page.open_url()
    main_page.click_on_currency_dropdown()
    main_page.click_on_euro_button()
    main_page.check_product_price_contains_euro()
    main_page.click_on_currency_dropdown()
    main_page.click_on_dollar_button()
    main_page.check_product_price_contains_dollar()

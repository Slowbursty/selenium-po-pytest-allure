import allure
import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.story('Проверка смены картинок в слайдере')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_slide_main_page_pictures(browser):
    main_page = MainPage(browser)
    product_page = ProductPage(browser)

    main_page.open_url()
    main_page.click_on_mac_book_product()
    product_page.click_on_main_picture()
    product_page.click_next_and_check_slider()

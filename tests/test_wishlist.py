import allure
import pytest

from pages.main_page import MainPage
from pages.phones_and_pda_page import PhonesAndPdaPage
from pages.product_page import ProductPage


@allure.story('Проверка добавления в избранное')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_add_to_wishlist_when_not_register(browser):
    main_page = MainPage(browser)
    phones_and_pda_page = PhonesAndPdaPage(browser)
    product_page = ProductPage(browser)

    main_page.open_url()
    main_page.click_on_phones_and_pda()
    phones_and_pda_page.click_on_htc_touch_hd()
    product_page.click_on_add_wishlist()
    product_page.check_alert("You must login or create an account to save HTC Touch HD to your wish list!")

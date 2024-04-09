import allure
import pytest

from pages.main_page import MainPage
from pages.phones_and_pda_page import PhonesAndPdaPage
from pages.product_page import ProductPage


@allure.story('Проверка добавления HTC в корзину')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_add_htc_to_cart(browser):
    main_page = MainPage(browser)
    phones_and_pda_page = PhonesAndPdaPage(browser)
    product_page = ProductPage(browser)

    main_page.open_url()
    main_page.click_on_phones_and_pda()
    phones_and_pda_page.click_on_htc_touch_hd()
    product_page.click_on_add_to_cart()
    product_page.check_alert("Success: You have added HTC Touch HD to your shopping cart!")

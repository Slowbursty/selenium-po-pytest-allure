import allure
import pytest

from pages.main_page import MainPage
from pages.tablets_page import TabletsPage


@allure.story('Проверка добавления планшета в корзину')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_add_tablet_to_cart(browser):
    main_page = MainPage(browser)
    tablets_page = TabletsPage(browser)

    main_page.open_url()
    main_page.click_tablets()
    tablets_page.add_samsung_tablet_to_cart()
    tablets_page.check_alert("Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!")

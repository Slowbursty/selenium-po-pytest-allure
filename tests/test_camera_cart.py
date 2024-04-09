import allure
import pytest

from pages.cameras_page import CamerasPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.story('Проверка добавления камеры в корзину')
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_add_camera_to_cart(browser):
    main_page = MainPage(browser)
    cameras_page = CamerasPage(browser)
    product_page = ProductPage(browser)

    main_page.open_url()
    main_page.click_cameras()
    cameras_page.click_on_nikon_product()
    product_page.click_on_add_to_cart()
    product_page.check_alert("Success: You have added Nikon D300 to your shopping cart!")

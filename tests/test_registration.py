import allure
import pytest

from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@allure.story("Проверка регистрации")
@pytest.mark.parametrize("browser", ["firefox", "chrome"], indirect=True)
def test_registration(browser):
    main_page = MainPage(browser)
    registration_page = RegistrationPage(browser)

    main_page.open_url()
    main_page.click_on_account_dropdown()
    main_page.click_on_register()
    registration_page.fill_form()
    registration_page.click_checkbox()
    registration_page.click_button_submit()
    registration_page.check_registration_form()

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TabletsPage(BasePage):
    alert = (By.XPATH, "//div[contains(@class, 'alert')]")
    add_to_cart_button = (By.XPATH, "//button[@aria-label='Add to Cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_samsung_tablet_to_cart(self):
        self.find_element(self.add_to_cart_button)
        self.click_on(self.add_to_cart_button)

    def check_alert(self, alert_message):
        with allure.step(f'Проверить, что отображается алерт «{alert_message}»'):
            self.check_alert_text_element(self.alert, alert_message)

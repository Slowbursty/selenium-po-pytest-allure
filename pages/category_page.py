import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    notification_text = (By.XPATH, "//h2[text()='PC']//following-sibling::p")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_pc_is_empty(self):
        text_when_empty = "There are no products to list in this category."

        with allure.step(f'Проверить, что отображается текст «{text_when_empty}»'):
            assert self.find_element(self.notification_text).text == text_when_empty

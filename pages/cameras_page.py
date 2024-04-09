from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CamerasPage(BasePage):
    nikon_product = (By.XPATH, "//a[text()='Nikon D300']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_nikon_product(self):
        self.find_element(self.nikon_product)
        self.click_on(self.nikon_product)

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PhonesAndPdaPage(BasePage):
    htc_touch_hd_product = (By.XPATH, "//a[text()='HTC Touch HD']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_htc_touch_hd(self):
        self.find_element(self.htc_touch_hd_product)
        self.click_on(self.htc_touch_hd_product)

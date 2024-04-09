from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    input_first_name = (By.XPATH, "//input[@id='input-firstname']")
    input_last_name = (By.XPATH, "//input[@id='input-lastname']")
    input_email = (By.XPATH, "//input[@id='input-email']")
    input_password = (By.XPATH, "//input[@id='input-password']")
    checkbox = (By.XPATH, "//input[@class='form-check-input']")
    button_submit = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker()

    def fill_form(self):
        self.send_keys_input(self.input_first_name, self.faker.first_name())
        self.send_keys_input(self.input_last_name, self.faker.last_name())
        self.send_keys_input(self.input_email, self.faker.email())
        self.send_keys_input(self.input_password, self.faker.password())

    def click_checkbox(self):
        self.find_element(self.checkbox)
        self.click_on(self.checkbox)

    def click_button_submit(self):
        self.find_element(self.button_submit)
        self.click_on(self.button_submit)

    def check_registration_form(self):
        assert self.find_element(self.input_first_name).text == ""
        assert self.find_element(self.input_last_name).text == ""
        assert self.find_element(self.input_email).text == ""
        assert self.find_element(self.input_password).text == ""

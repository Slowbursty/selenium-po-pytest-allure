import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://demo.opencart.com/"
    mac_book_product = (By.XPATH, "//a[text()='MacBook']")
    product_page_main_picture = (By.XPATH, "//img[@title='MacBook']//parent::a")
    next_picture_button = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    first_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_1')]")
    second_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_3')]")
    third_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_2')]")
    fourth_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_4')]")
    fifth_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_5')]")
    currency_dropdown = (By.XPATH, "//span[contains(., 'Currency')]/following-sibling::i")
    dropdown_menu = (By.XPATH, "//ul[@class='dropdown-menu show']")
    dropdown_euro_button = (By.XPATH, "//a[contains(text(), 'Euro')]")
    dropdown_dollar_button = (By.XPATH, "//a[contains(text(), 'US Dollar')]")
    product_card_price = (By.XPATH, "//span[@class='price-new']")
    desktops = (By.XPATH, "//a[text()='Desktops']")
    phones_pda = (By.XPATH, "//a[text()='Phones & PDAs']")
    cameras = (By.XPATH, "//a[text()='Cameras']")
    tablets = (By.XPATH, "//a[text()='Tablets']")
    pc = (By.XPATH, "(//a[text()='PC (0)'])[2]")
    body = (By.XPATH, "//body")
    account_dropdown = (By.XPATH, "//span[text()='My Account']")
    register = (By.XPATH, "//a[text()='Register']")
    search = (By.XPATH, "//input[@placeholder='Search']")
    search_button = (By.XPATH, "//input[@placeholder='Search']/following-sibling::button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_url(self):
        self.open(self.URL)

    def click_on_mac_book_product(self):
        self.find_element(self.product_page_main_picture)
        self.click_on(self.product_page_main_picture)

    def click_next_and_check_slider(self):
        pictures = [self.first_picture, self.second_picture, self.third_picture, self.fourth_picture, self.fifth_picture]

        for pic in pictures:
            assert self.find_element(pic).is_displayed()
            self.click_on(self.next_picture_button)

    def click_on_currency_dropdown(self):
        self.browser_refresh()
        self.browser_refresh()
        self.browser_refresh()
        self.find_element(self.currency_dropdown)
        self.browser.execute_script("document.getElementsByClassName('fas fa-caret-down')[0].click()")

        if self.browser.current_url.__contains__("#"):
            time.sleep(2)
            self.find_element(self.currency_dropdown)
            self.click_on(self.currency_dropdown)

        self.find_element(self.dropdown_menu)

    def click_on_euro_button(self):
        self.find_element(self.dropdown_euro_button)
        self.click_on(self.dropdown_euro_button)

    def click_on_dollar_button(self):
        self.find_element(self.dropdown_dollar_button)
        self.click_on(self.dropdown_dollar_button)

    def check_product_price_contains_euro(self):
        self.find_element(self.product_card_price).text.__contains__("€")

    def check_product_price_contains_dollar(self):
        self.find_element(self.product_card_price).text.__contains__("$")

    def click_on_desktops(self):
        self.find_element(self.desktops)
        self.click_on(self.desktops)
        self.find_element(self.body)
        self.click_on(self.body)

    def click_on_pc(self):
        self.find_element(self.pc)
        self.click_on(self.pc)

    def click_on_account_dropdown(self):
        self.find_element(self.account_dropdown)
        self.click_on(self.account_dropdown)

    def click_on_register(self):
        self.find_element(self.register)
        self.click_on(self.register)
        self.wait_url_contains("/register")

    def fill_search_field(self):
        self.find_element(self.search)
        self.send_keys_input(self.search, "macbook")

    def click_on_search(self):
        self.find_element(self.search_button)
        self.click_on(self.search_button)

    def click_on_phones_and_pda(self):
        self.find_element(self.phones_pda)
        self.click_on(self.phones_pda)

    def click_cameras(self):
        self.find_element(self.cameras)
        self.click_on(self.cameras)

    def click_tablets(self):
        self.find_element(self.tablets)
        self.click_on(self.tablets)

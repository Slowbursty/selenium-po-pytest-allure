import allure
from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    fullscreen_picture = (By.XPATH, "//body/img[contains(@src, 'macbook_1')]")
    product_page_main_picture = (By.XPATH, "//img[@title='MacBook']//parent::a")
    next_picture_button = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    first_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_1')]")
    second_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_3')]")
    third_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_2')]")
    fourth_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_4')]")
    fifth_picture = (By.XPATH, "//div[@class='mfp-content']//img[contains(@src, 'macbook_5')]")
    add_wish_list_button = (By.XPATH, "//button[@aria-label='Add to Wish List']")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to Cart']")
    alert = (By.XPATH, "//div[contains(@class, 'alert')]")
    review_tab = (By.XPATH, "//a[contains(text(), 'Reviews')]")
    reviewer_input_name = (By.XPATH, "//input[@id='input-name']")
    reviewer_textarea = (By.XPATH, "//textarea[@id='input-text']")
    reviewer_rating_star_3 = (By.XPATH, "//input[@value='3']")
    reviewer_button_continue = (By.XPATH, "//button[@id='button-review']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker()

    def click_on_main_picture(self):
        self.find_element(self.product_page_main_picture)
        self.click_on(self.product_page_main_picture)
        self.wait_url_contains("https://demo.opencart.com/image/cache/catalog/demo/macbook_1-800x800.jpg")
        self.visibility_of_element_located(self.fullscreen_picture)
        self.browser_back()
        self.find_element(self.product_page_main_picture)
        self.click_on(self.product_page_main_picture)

    def click_next_and_check_slider(self):
        pictures = [self.first_picture, self.second_picture, self.third_picture, self.fourth_picture, self.fifth_picture]

        for pic in pictures:
            with allure.step(f'Проверить, что отображается картинка «{pic}»'):
                assert self.find_element(pic).is_displayed()
            with allure.step(f'Нажать на кнопку Следующая «{self.next_picture_button}»'):
                assert self.click_on(self.next_picture_button)

    def click_on_add_wishlist(self):
        self.browser_refresh()
        self.find_element(self.add_wish_list_button)
        self.click_on(self.add_wish_list_button)

    def click_on_add_to_cart(self):
        self.browser_refresh()
        self.find_element(self.add_to_cart_button)
        self.click_on(self.add_to_cart_button)

    def check_alert(self, alert_message):
        with allure.step(f'Проверить, что отображается алерт «{alert_message}»'):
            self.check_alert_text_element(self.alert, alert_message)

    def click_on_review(self):
        self.find_element(self.review_tab)
        self.click_on(self.review_tab)

    def fill_review_form(self):
        self.send_keys_input(self.reviewer_input_name, "DemoReviewer")
        self.send_keys_input(self.reviewer_textarea, self.faker.text(max_nb_chars=100))
        self.click_on(self.reviewer_rating_star_3)

    def click_continue_button(self):
        self.click_on(self.reviewer_button_continue)

    def check_alert_review(self):
        success_alert_submit_review = "Thank you for your review. It has been submitted to the webmaster for approval."

        with allure.step(f'Проверить, что отображается алерт «{success_alert_submit_review}»'):
            self.check_alert_text_element(self.alert, success_alert_submit_review)

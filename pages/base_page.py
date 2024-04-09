import logging
import os
from datetime import datetime

import allure
from assertpy import assert_that
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://demo.opencart.com/"
        self.__config_logger()

    def get_logger(self):
        return self.logger

    def __config_logger(self, to_file=True):
        self.logger = logging.getLogger(type(self).__name__)

        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log", encoding='utf-8'))
        self.logger.setLevel(level=self.browser.log_level)

    def open(self, url):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.logger.info("============= Start test: «{}»".format(now))
        with allure.step(f'Открытие страницы «{url}»'):
            self.logger.info("Opening url: «{}»".format(url))
            self.browser.get(url)

    def find_element(self, locator, timeout=10):
        with allure.step(f'Поиск элемента «{locator}»'):
            self.logger.info("Finding element: «{}»".format(locator))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                raise AssertionError(f"Can't find elements by locator {locator}")

    def visibility_of_element_located(self, locator, timeout=10):
        with allure.step(f'Проверка видимости элемента «{locator}»'):
            self.logger.info("Checking element is visible: «{}»".format(locator))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError(f"Can't find elements by locator {locator}")

    def wait_url_contains(self, url, timeout=10):
        with allure.step(f'Проверка URL, содержащего «{url}»'):
            self.logger.info("Checking url: «{}»".format(url))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.url_contains(url))
            except TimeoutException:
                raise AssertionError(f"Can't find {url}")

    def click_on(self, locator, timeout=10):
        with allure.step(f'Клик по элементу «{locator}»'):
            self.logger.info("Check element is clickable and clicking on element: «{}»".format(locator))
            try:
                element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
                self.browser.execute_script("arguments[0].scrollIntoView();", element)
                return element.click()
            except TimeoutException:
                raise AssertionError(f"Can't find elements by locator {locator}")

    def browser_back(self):
        with allure.step('Возврат на предыдущую страницу'):
            self.logger.info("Browser back")
            self.browser.back()

    def browser_refresh(self):
        with allure.step('Обновить текущую страницу'):
            self.logger.info("Browser refresh")
            self.browser.refresh()

    def send_keys_input(self, locator, text):
        with allure.step(f'Ввод текста «{text}»'):
            self.logger.info("Send keys: «{}»".format(text))
            self.find_element(locator).send_keys(text)

    def check_alert_text_element(self, locator, text):
        with allure.step(f'Проверка текста «{text}»'):
            self.logger.info("Checking alert text: «{}»".format(text))
            assert_that(self.visibility_of_element_located(locator).get_attribute("innerText")).contains(text)

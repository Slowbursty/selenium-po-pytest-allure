import json
import logging

import allure
import pytest
from selenium import webdriver

from pages.base_page import BasePage


@pytest.fixture
def browser(request):
    if request.param == "chrome":
        driver_browser = init_chrome()
    elif request.param == "firefox":
        driver_browser = init_firefox()
    else:
        raise ValueError("Unsupported browser!")

    # этот код прикрепит аттачи с параметрами setup'a браузера
    # allure.attach(
    #     name=driver_browser.session_id,
    #     body=json.dumps(driver_browser.capabilities, indent=4, ensure_ascii=False),
    #     attachment_type=allure.attachment_type.JSON)

    driver_browser.test_name = request.node.name
    driver_browser.log_level = logging.DEBUG
    yield driver_browser

    BasePage(driver_browser).get_logger().handlers.clear()

    # всегда создает скриншоты в конце теста вне зависимости от статуса теста [passed/failed/skipped]
    allure.attach(
        name="screenshot",
        body=driver_browser.get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG
    )

    # всегда копирует DOM страницу в конце теста вне зависимости от статуса теста [passed/failed/skipped]
    allure.attach(
        name="page_source",
        body=driver_browser.page_source,
        attachment_type=allure.attachment_type.HTML
    )

    driver_browser.quit()


def init_chrome():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # driver_browser = webdriver.Chrome(options=options)
    driver_browser = webdriver.Chrome()
    base_config(driver_browser)
    return driver_browser


def init_firefox():
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # driver_browser = webdriver.Firefox(options=options)
    driver_browser = webdriver.Firefox()
    base_config(driver_browser)
    return driver_browser


def base_config(driver_browser):
    driver_browser.implicitly_wait(20)
    driver_browser.maximize_window()

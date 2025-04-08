import os
import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()


@pytest.fixture()
def driver():
    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options = options)
    _driver.get(os.getenv("WEBSITE_URL"))
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function", autouse=True)
def create_customers(add_customer_page, generator):
    for _ in range(2):
        code = generator.generate_code()
        name = generator.generate_name(code)

        add_customer_page.open_page()
        add_customer_page.insert_first_name(name)
        add_customer_page.insert_last_name("Popova")
        add_customer_page.insert_postcode(code)
        add_customer_page.confirm_adding()
        add_customer_page.handle_alert()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is not None:
                allure.attach(
                    item.funcargs.get('driver').get_screenshot_as_png(),
                    name='Скриншот',
                    attachment_type=allure.attachment_type.PNG
                )

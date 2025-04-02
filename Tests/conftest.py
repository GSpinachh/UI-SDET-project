import pytest


from Services.generator import Generator
from Services.customers_handler import CustomersHandler
from Pages.add_customer_page import AddCustomerPage
from Pages.customer_page import CustomersPage


@pytest.fixture()
def generator():
    return Generator()


@pytest.fixture()
def customers_handler():
    return CustomersHandler()


@pytest.fixture()
def add_customer_page(driver):
    return AddCustomerPage(driver)


@pytest.fixture()
def customers_page(driver):
    return CustomersPage(driver)
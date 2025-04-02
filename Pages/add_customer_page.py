import os


import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


from Pages.base_page import BasePage


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=os.getenv('TIMEOUT'))

        self.customer_btn = (By.XPATH, '//button[normalize-space()="Add Customer"]')
        self.first_name = (By.XPATH, '//input[@placeholder="First Name"]')
        self.last_name = (By.XPATH, '//input[@placeholder="Last Name"]')
        self.post_code = (By.XPATH, '//input[@placeholder="Post Code"]')
        self.confirm_btn = (By.XPATH, '//button[@type="submit"]')

    @allure.step(f'Открыть страницу добавления клиента кнопкой "Add Customer"')
    def open_page(self) -> None:
        self.find_element(*self.customer_btn).click()

    @allure.step(f'Ввести код в поле "Post Code"')
    def insert_postcode(self, code: str) -> None:
        self.find_element(*self.post_code).send_keys(code)

    @allure.step(f'Ввести имя в поле "First Name"')
    def insert_first_name(self, name: str) -> None:
        self.find_element(*self.first_name).send_keys(name)

    @allure.step(f'Ввести фамилию в поле "Last Name"')
    def insert_last_name(self, surname: str) -> None:
        self.find_element(*self.last_name).send_keys(surname)

    @allure.step(f'Нажать кнопку подтверждения "Add Customer"')
    def confirm_adding(self):
        self.find_element(*self.confirm_btn).click()

    @allure.step(f'Закрыть всплывающее уведомление')
    def handle_alert(self):
        alert = Alert(self.driver)
        text = alert.text
        alert.accept()
        return text
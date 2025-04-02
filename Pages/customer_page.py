import os


import allure
from selenium.webdriver.common.by import By


from Pages.base_page import BasePage


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=os.getenv('TIMEOUT'))

        self.customers_button = (By.XPATH, '//button[normalize-space()="Customers"]')
        self.first_name = (By.XPATH, '//a[normalize-space()="First Name"]')
        self.name_list = (By.XPATH, '//td[@class="ng-binding"][1]')
        self.delete_buttons = (By.XPATH, '//button[@ng-click="deleteCust(cust)"]')

    @allure.step('Открыть страницу клиентов кнопкой "Customers"')
    def open_page(self) -> None:
        self.find_element(*self.customers_button).click()

    @allure.step('Нажать кнопку "First Name" для сортировки списка')
    def sort_names(self, a_z_sort: bool) -> None:
        self.find_element(*self.first_name).click()
        if a_z_sort:
            self.find_element(*self.first_name).click()

    @allure.step('Получить список имён пользователей')
    def get_customer_names(self) -> list[str]:
        names = self.find_elements(*self.name_list)
        return [name.text for name in names]
    
    @allure.step('Удалить клиента')
    def delete_customer(self, name):
        buttons = self.find_elements(*self.delete_buttons)
        names = self.find_elements(*self.name_list)
        position = [name.text for name in names].index(name)
        buttons[position].click()
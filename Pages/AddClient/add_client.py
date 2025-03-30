import allure
from selenium.webdriver.common.alert import Alert

from Services.base_page import BasePage
from Services.string_manipulator import StringManipulator
from Pages.AddClient.add_client_locators import AddClientLocators
from Pages.customer_management import add_customer, post_code, first_name, last_name, customers


class AddClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    str_manipulator = StringManipulator()

    @allure.step(f'Открыть целевую страницу')
    def open_target_page(self) -> None:
        self.open_page(AddClientLocators.page_url)

    @allure.step(f'Нажать кнопку "{add_customer}"')
    def click_add_customer(self) -> None:
        self.click_element(AddClientLocators.customer_btn)

    @allure.step(f'Ввести код в поле "{post_code}"')
    def insert_postcode(self, code: str) -> None:
        code = str(code)
        self.insert_value(AddClientLocators.post_code_field, code)

    @allure.step(f'Ввести имя в поле "{first_name}"')
    def insert_first_name(self, code: str) -> None:
        self.insert_value(AddClientLocators.first_name_field, self.str_manipulator.extract_name_from_code(code))

    @allure.step(f'Ввести фамилию в поле "{last_name}"')
    def insert_last_name(self, code: str) -> None:
        self.insert_value(AddClientLocators.last_name_field, self.str_manipulator.extract_surname_from_code(code))

    @allure.step(f'Заполнить все поля с информацией о пользователе')
    def fill_all_fields(self, code: str) -> None:
        self.insert_first_name(code)
        self.insert_last_name(code)
        self.insert_postcode(code)

    @allure.step(f'Нажать кнопку подтверждения "{add_customer}"')
    def confirm_adding(self):
        self.click_element(AddClientLocators.confirm_btn)

    @allure.step(f'Закрыть всплывающее уведомление')
    def close_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    @allure.step(f'Нажать кнопку "{customers}"')
    def click_customers_btn(self) -> None:
        self.click_element(AddClientLocators.customers_btn)

    @allure.step(f'Проверить, что новый пользователь появился')
    def check_new_customer_existence(self, code: str):
        self.find_element(AddClientLocators.new_customer_name(
            self.str_manipulator.extract_name_from_code(code)))

        self.find_element(AddClientLocators.new_customer_surname(
            self.str_manipulator.extract_surname_from_code(code)))

        self.find_element(AddClientLocators.new_customer_code(code))
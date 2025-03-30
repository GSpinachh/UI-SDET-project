import allure

from Services.base_page import BasePage
from Pages.DeleteClient.delete_client_locators import DeleteClientLocators
from Pages.customer_management import customers, post_code

class DeleteClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    @allure.step('Открыть целевую страницу')
    def open_target_page(self) -> None:
        self.open_page(DeleteClientLocators.page_url)

    @allure.step(f'Нажать кнопку "{customers}"')
    def click_customers_btn(self) -> None:
        self.click_element(DeleteClientLocators.customers_btn)

    @allure.step('Получить список имён пользователей')
    def get_names_list(self) -> list[str]:
        return [self.get_element_text(DeleteClientLocators.customer_name(i)) 
                for i in range(1, len(self.find_elements(DeleteClientLocators.customers_list)) + 1)]

    @allure.step('Узнать длину каждого имени')
    def get_names_len(self) -> list[int]:
        return [len(name) for name in self.get_names_list()]

    @allure.step('Посчитать среднюю длину имени')
    def calc_avg_len(self) -> float:
        names_len = self.get_names_len()
        return sum(names_len) / len(names_len) if names_len else 0.0

    @allure.step('Найти пользователя, у которого длина имени ближе к среднему арифметическому')
    def find_optimal_customer(self) -> list[int]:
        names_len = self.get_names_len()
        avg_len = self.calc_avg_len()
        diff_list = [abs(avg_len - length) for length in names_len]
        min_value = min(diff_list)
        return [i for i, diff in enumerate(diff_list) if diff == min_value]

    @allure.step(f'Получить "{post_code}" удаляемых пользователей')
    def get_deletion_customer_code(self, customer_ids: list[int]) -> list[str]:
        return [self.get_element_text(DeleteClientLocators.get_customer_code(customer_id)) 
                for customer_id in customer_ids]

    @allure.step('Удалить пользователя, у которого длина имени ближе к среднему арифметическому')
    def delete_customer(self, customer_ids: list[int]) -> None:
        for customer_id in reversed(customer_ids):
            self.click_element(DeleteClientLocators.delete_customer_btn(customer_id))

    @allure.step('Проверить удаление пользователя')
    def check_successful_deletion(self, customer_codes: list[str]) -> None:
        matches = [self.check_presence_of_element(DeleteClientLocators.get_deleted_customer_locator(code)) 
                   for code in customer_codes]
        assert not any(matches), (
            '[ERROR] Один или несколько пользователей не было удалено'
        )

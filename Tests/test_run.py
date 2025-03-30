import allure
import pytest

from Services.generator import Generator
from Pages.AddClient.add_client import AddClient
from Pages.DeleteClient.delete_client import DeleteClient
from Pages.SortClients.sort_clients import SortClients


@allure.suite('Тесты')
class Tests:
    @allure.title('Добавить пользователя')
    def test_add_customer(self, driver):
        customer_driver = AddClient(driver)

        customer_driver.open_target_page()
        code = Generator.generate_code()
        customer_driver.click_add_customer()
        customer_driver.fill_all_fields(code)
        customer_driver.confirm_adding()
        customer_driver.close_alert()
        customer_driver.click_customers_btn()
        customer_driver.check_new_customer_existence(code)

    @allure.title('Сортировать пользователей по имени')
    def test_sort_customers(self, driver):
        sort_driver = SortClients(driver)

        sort_driver.open_target_page()
        sort_driver.click_customers_btn()
        sort_driver.click_first_name_btn()
        sort_driver.click_first_name_btn() 

        sort_driver.check_names_list()

    @allure.title('Удалить пользователя, у которого длина имени ближе к среднему арифметическому')
    def test_delete_customer(self, driver):
        del_driver = DeleteClient(driver)

        del_driver.open_target_page()
        del_driver.click_customers_btn()
        customer_id = del_driver.find_optimal_customer()
        del_codes = del_driver.get_deletion_customer_code(customer_id)
        del_driver.delete_customer(customer_id)
        del_driver.check_successful_deletion(del_codes)
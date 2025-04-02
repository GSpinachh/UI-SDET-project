import allure


class Tests:
    @allure.title('Добавить пользователя')
    @staticmethod
    def test_add_customer(add_customer_page, customers_page, generator):
        add_customer_page.open_page()

        code = generator.generate_code()
        name = generator.generate_name(code)

        add_customer_page.insert_first_name(name)
        add_customer_page.insert_last_name("Popova")
        add_customer_page.insert_postcode(code)
        add_customer_page.confirm_adding()

        alert_text = add_customer_page.handle_alert()

        with allure.step('Смотрим если клиент добавился по выводу окна'):
            assert 'Customer added successfully' in alert_text, (
                f'Ошибка при добавлении клиента, "{alert_text}"'
                )
        
        customers_page.open_page()
        
        name_list = customers_page.get_customer_names()

        with allure.step('Смотрим если клиент в списке.'):
            assert name in name_list, (
                f'Клиент "{name}" не найден в списке.'
            )

    @allure.title('Сортировать пользователей по имени')
    @staticmethod
    def test_sort_customers(customers_page):
        customers_page.open_page()

        a_z_sort = True
        customers_page.sort_names(a_z_sort)

        names = customers_page.get_customer_names()
        sorted_names = sorted(names, key=str.lower)

        with allure.step('Смотрим если клиент добавился в список'):
            assert names == sorted_names if a_z_sort else reversed(sorted_names), (
            'Список не отсортирован по алфавиту'
        )


    @allure.title('Удалить пользователя, у которого длина имени ближе к среднему арифметическому')
    @staticmethod
    def test_delete_customer(customers_page, customers_handler):
        customers_page.open_page()

        names = customers_page.get_customer_names()
        selected_customer = customers_handler.get_fitting_name(names)
        customers_page.delete_customer(selected_customer)

        name_list = customers_page.get_customer_names()

        with allure.step('Смотрим если клиент удалился из списка'):
            assert not (selected_customer in name_list), (
                'Клиент не удалился из списка'
                )
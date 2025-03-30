# UI-SDET-project

Практикум SDET simbirsoft: задание UI

Объект тестирования: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager

Задание

Составить подробные тест-кейсы по чек-листу из 3 кейсов, описанном далее.
На языке программирования Java (версия 11 или 17) или Python (версия 3.10) создать проект UI-автотестов по тест-кейсам. Кейсы также прикрепить в данный проект (в формате текстового файла с использованием Markdown).
В проекте использовать: Selenium Webdriver (желательно использовать браузер Chrome) Один из тестовых фреймворков: Java - TestNG, JUnit 4/5, Python - pytest Один из сборщиков (для Java): Maven, Gradle.
Результаты на проверку оформить в виде Merge Request/Pull Request (!!!) ветки в которой вы вели разработку в главную на Gitlab/GitHub
Дополнительное задание №1: Реализовать формирование отчетов Allure.
Дополнительное задание №2: Реализовать параллельный запуск тестов.
Дополнительное задание №3: Реализовать запуск в системе CI/CD.
Чек-лист:

Создание клиента (Add Customer). При создании тестовых данных для полей Post Code и First Name необходимо: 1.1 для поля Post Code сгенерировать номер из 10 цифр 1.2 для поля First Name сгенерировать имя на основе Post Code согласно следующей логике:

1 ) Post Code условно разбиваем на двузначные цифры (получится 5 цифр)

2 ) Каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25. Если цифра больше 25, то начинаем с 26 как с 0. Т.е. 0 - a, 26 - тоже a, 52 – тоже a, и т.д. Пример: 0001252667 = abzap

Сортировка клиентов по имени (First Name).

Удаление клиента. При поиске клиента на удаление необходимо: Получить из таблицы Customers список имен. Узнать длину каждого имени, затем найти среднее арифметическое получившихся длин и удалить клиента с тем именем, у которого длина будет ближе к среднему арифметическому (для Java требуется использовать Stream API). Пример: список имен - Albus, Neville, Voldemort. Длины имен – 5, 7, 9 соответственно. Среднее арифметическое длин – 7, удаляем имя Neville.

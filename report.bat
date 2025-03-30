if exist allure-results (
   rmdir /s /q allure-results
)
pytest --alluredir allure-results
allure serve allure-results
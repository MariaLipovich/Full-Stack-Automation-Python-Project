import allure
import pytest
# Selenium 4.1.0
# Change UrlWeb in conftest to 'Avengers' before running tests
# runnung tests in the terminal:
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_database.py --alluredir=./allure-report_database
# allure serve allure-report_database

from workflows.database_web_flows import DatabaseWebFlows

@pytest.mark.usefixtures('_init_web_driver')
@pytest.mark.usefixtures('_init_connector_database')
class TestDatabase:
    @allure.title('Iron Man Movie Page')
    @allure.description('This test checks whether the input fields are filled in correctly to go to the movie page')
    def test_iron_man(self):
        DatabaseWebFlows.verify_iron_man_page()
        DatabaseWebFlows.fill_data()

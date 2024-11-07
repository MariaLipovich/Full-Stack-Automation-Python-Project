import datetime
import time

import allure
import pytest
from workflows.electron_flows import ElectronFlows

# running tests in the terminal:
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_electron.py --alluredir=./allure-report_electron_jenkins
# allure serve allure-report_electron


@pytest.mark.usefixtures('_init_electron_driver')
class TestElectron:

    @allure.title("Verify Today`s Date")
    @allure.description("This test verify that today`s date display in the main page")
    def test_verify_today_date(self):
        ElectronFlows.verify_date(str(datetime.date.today()))

    @allure.title("Create Task")
    @allure.description("This test verify that task was created")
    def test_create_task(self):
        ElectronFlows.create_task("To clean an apartment")
        ElectronFlows.create_task("To cook a soup")
        ElectronFlows.create_task("Yoga")
        ElectronFlows.verify_tasks(3)
        ElectronFlows.click_on_delete_tasks()

    @allure.title("Complete One Task")
    @allure.description("This test verify remaining tasks count if one task was completed ")
    def test_complete_one_task(self):
        ElectronFlows.create_task("To clean an apartment")
        ElectronFlows.create_task("To cook a soup")
        ElectronFlows.create_task("Yoga")
        ElectronFlows.verify_tasks(3)
        ElectronFlows.completing_task(1)
        ElectronFlows.verify_all_remaining_tasks('2')
        ElectronFlows.click_on_delete_tasks()

    @allure.title("Complete All Tasks")
    @allure.description("This test verify remaining tasks count if all tasks were completed ")
    def test_complete_all_tasks(self):
        ElectronFlows.create_task("To clean an apartment")
        ElectronFlows.create_task("To cook a soup")
        ElectronFlows.create_task("Yoga")
        ElectronFlows.verify_tasks(3)
        ElectronFlows.click_on_all_completed()
        ElectronFlows.verify_all_remaining_tasks('0')
        ElectronFlows.click_on_delete_tasks()

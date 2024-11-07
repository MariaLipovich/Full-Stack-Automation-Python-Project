import allure
import pytest

from workflows.desktop_flows import DesktopFlows
# running tests in the terminal:
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_desktop.py --alluredir=./allure-report_desktop
# allure serve allure-report_desktop

@pytest.mark.usefixtures('_init_desktop_driver')
class TestDesktop:

    @allure.title('Test1:Change Calculator Type')
    @allure.description('This test changes calculator type')
    def test_change_type(self):
        DesktopFlows.change_calculator_type('Time')

    @allure.title('Test2:Convert Hours To Minutes')
    @allure.description("This test convert top line to hours and bottom line to minutes")
    def test_choose_measurement(self):
        DesktopFlows.unit_of_measurement_upper('Hours')
        DesktopFlows.unit_of_measurement_lower('Minutes')

    @allure.title('Test3Calculate Minutes In Hours')
    @allure.description('Convert hours in minutes, verify it, calculate and clear it')
    def test_calculate(self):
        DesktopFlows.get_numbers('10')
        DesktopFlows.verify_result('600')

    @allure.title('Test4:Clear Result')
    @allure.description('This test verify result as 0')
    def test_clear_result(self):
        DesktopFlows.clear_result('0')

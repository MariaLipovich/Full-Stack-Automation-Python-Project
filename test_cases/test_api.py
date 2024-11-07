import allure

from extensions.verifications import Verifications
from workflows.api_flows import API_flows

# running test in the terminal
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_api.py --alluredir=./allure-report_api
#allure serve allure-report_api


class Test_API:
    @allure.title("Test01: Get Users List And Verify Status Code")
    @allure.description("This test returns users list and verify status code")
    def test_users_list(self):
        actual_result = API_flows.get_users_list()
        Verifications.verify_equals(str(actual_result), '200')

    @allure.title("Test02: Register An User And Verify Status Code")
    @allure.description("This test returns id and token after an user register and verify status code")
    def test_user_register(self):
        actual_result = API_flows.register_user("eve.holt@reqres.in", "password0")
        Verifications.verify_equals(str(actual_result), '200')

    @allure.title("Test03: Get A Single User And Verify Status Code")
    @allure.description("This test returns a single user and verify status code")
    def test_single_user(self):
        actual_result = API_flows.get_user(5)
        Verifications.verify_equals(str(actual_result), '200')

    @allure.title("Test04: Verify Last Name before updating")
    @allure.description("This test returns verification last name")
    def test_last_name(self):
        nodes = ["data", 4, "last_name"]
        updating_last_name = API_flows.get_value_users_from_api(nodes)
        Verifications.verify_equals(updating_last_name, "Morris")

    @allure.title("Test05: Update A Single User And Verify Status Code")
    @allure.description("This test returns an updating single user and verify status code")
    def test_update_user(self):
        actual_result = API_flows.update_user_data(5, "charles.morris@reqres.in",
                                                   "Charles", "Smith", "https://reqres.in/img/faces/5-image.jpg")
        Verifications.verify_equals(str(actual_result), '201')

    @allure.title("Test06: Delete A Single User And Verify Status Code")
    @allure.description("This test returns deleted user id and verify status code")
    def test_delete_single_user(self):
        actual_result = API_flows.delete_user(5)
        Verifications.verify_equals(str(actual_result), '201')

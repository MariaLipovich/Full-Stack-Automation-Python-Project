import time

import allure
import pytest

from utilities.common import get_data
from workflows.atidstore_flows import AtidStoreWebFlows
import test_cases.conftest as conft

# activate terminal:
# python -m venv venv
# venv\Scripts\activate
# install all packages from requirements.txt:
# pip install -r requirements.txt
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_web_atidstore.py --alluredir=./allure-report
# allure serve allure-report


@pytest.mark.usefixtures('_init_web_driver')
class TestWebAtidStore:

    @allure.title('Test01: Verify Main Page Menu on Atid Store')
    @allure.description('This test verifies whether the elements of the menu are displayed')
    def test_verify_main_page_menu(self):
        AtidStoreWebFlows.verify_main_page()

    @allure.title('Test02: Verify Count The Items')
    @allure.description('This test verifies store page and count the number of items on the page')
    def test_verify_items(self):
        AtidStoreWebFlows.verify_store()
        AtidStoreWebFlows.count_items()

    @allure.title('Test03: Verify Items In Shopping Cart And Checkout Page')
    @allure.description('This test verifies whether the items in Shopping cart and moving to checkout page')
    def test_verify_items_in_cart(self):
        AtidStoreWebFlows.add_item(1)
        AtidStoreWebFlows.store_page()
        AtidStoreWebFlows.add_item(2)
        AtidStoreWebFlows.store_page()
        AtidStoreWebFlows.add_item(3)
        AtidStoreWebFlows.store_page()
        AtidStoreWebFlows.verify_count_items('3')
        AtidStoreWebFlows.checkout_page()

    @allure.title('Test04: Verify Checkout page')
    @allure.description('Test verifies error message with incorrect and correct login data')
    @pytest.mark.parametrize('email, password, error_message', AtidStoreWebFlows.data)
    def test_checkout_process(self, email, password, error_message):
        AtidStoreWebFlows.login()
        AtidStoreWebFlows.input_csv_username_or_email_data(email)
        AtidStoreWebFlows.input_csv_password_data(password)
        AtidStoreWebFlows.login_button_atidstore()
        AtidStoreWebFlows.verify_expected_message(error_message)

    @allure.title('Test5: Visual Testing')
    @allure.description('This test verifies whether the elements of the store page are displayed')
    @pytest.mark.skipif(get_data('ExecuteApplitools') == "False",
                        reason='The test passed with selenium 3.141.0 and without EventFiringWebDriver()')
    def test_verify_store_page_for_applitools(self):
        conft.eyes.open(self.driver, 'Store Page', 'Verify Store Page On AtidStore')
        conft.driver.get("https://atid.store/store")
        AtidStoreWebFlows.verify_store()
        time.sleep(3)
        conft.eyes.check_window('Store page test')








import allure
import pytest

import test_cases.conftest as conft
from utilities.common import read_csv, get_data
from workflows.webflows import Webflows

# activate terminal:
# python -m venv venv
# venv\Scripts\activate
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_web.py --alluredir=./allure-results
# allure serve allure-result


@pytest.mark.usefixtures('_init_web_driver')
class TestWeb:
    @allure.title('Test1: Verify Main Page Menu on NopCommerce')
    @allure.description('This test verifies whether the elements of the menu are displayed')
    def test_verify_main_page_menu(self):
        Webflows.verify_main_page_menu()
        # Webflows.verify_main_page_menu_with_smart_assert()


    @allure.title('Verify Main Page with Logo')
    @allure.description('This method runs after each test and verifies the logo on the main page')
    def teardown_method(self):
        Webflows.main_page(self)

    @allure.title('Test2: Verify Empty Shopping Cart')
    @allure.description('This test verifies the empty shopping cart and checks for the appropriate message')
    def test_verify_shopping_cart_before_adding_items(self):
        Webflows.verify_main_page()
        Webflows.from_main_page_to_shopping_cart('Shopping cart')
        Webflows.verify_empty_shopping_cart_message()

    @allure.title('Test3: Add Three Notebooks to Shopping Cart')
    @allure.description('This test verifies that three notebooks were added to the shopping cart and checks for the appropriate message')
    def test_adding_item_to_shopping_cart(self):
        Webflows.verify_notebooks()
        Webflows.adding_notebook_to_shopping_cart(1)
        Webflows.adding_notebook_to_shopping_cart(2)
        Webflows.adding_notebook_to_shopping_cart(3)
        Webflows.shopping_cart_with_items(3)

    @allure.title('Test4: Remove Two Notebooks from Shopping Cart')
    @allure.description('This test verifies that after removing two items from the shopping cart, one item remains')
    def test_remove_item_from_shopping_cart(self):
        Webflows.from_main_page_to_shopping_cart('Shopping cart')
        Webflows.items_count(3)
        Webflows.item_in_shopping_cart(0)
        Webflows.item_in_shopping_cart(1)
        Webflows.items_count(1)

    @allure.title('Test5: Checkout')
    @allure.description('This test verifies the unsuccessful checkout process with invalid login data and checks for different error messages')
    @pytest.mark.parametrize('email, password, error_message', Webflows.data)
    def test_checkout_process(self, email, password, error_message):
        Webflows.from_main_page_to_shopping_cart('Shopping cart')
        Webflows.actions_after_choosing_items()
        Webflows.input_csv_email_data(email)
        Webflows.input_csv_password_data(password)
        Webflows.log_in_submit()
        Webflows.verify_expected_message(error_message)

    @allure.title('Test1: Verify Main Page Menu on NopCommerce')
    @allure.description('This test verifies whether the elements of the menu are displayed')
    @pytest.mark.skipif(get_data('ExecuteApplitools') == "False", reason='The test passed with selenium 3.141.0 and without EventFiringWebDriver()')
    def test_verify_main_page_menu_for_applitools(self):
        conft.eyes.open(self.driver, 'Test1',  'Verify Main Page Menu on NopCommerce')
        conft.driver.get("https://demo.nopcommerce.com/")
        Webflows.verify_main_page_menu()
        conft.eyes.check_window('Home page')

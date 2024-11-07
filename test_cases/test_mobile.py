
import pytest
import allure
from workflows.mobile_flows import MobileFlows

# running test in the terminal:
# pytest -s -v C:\development\PythonAtidAutomation\final_project_infrastructure\test_cases\test_mobile.py --alluredir=./allure-report_mobile
# allure serve allure-report_mobile


@pytest.mark.usefixtures('_init_mobile_driver')
class Test_Mobile:
    @allure.title('Verify The Home Page Button')
    @allure.description('This test verifies the home page button and moves from another page to the main page')
    def teardown_method(self):
        MobileFlows.home_page()

    @allure.title('Test01: Verify NopCommerce Home Page')
    @allure.description('this test verifies the home page')
    def test_verify_application_home_page(self):
        MobileFlows.popular_categories()
        MobileFlows.featured_products()
        MobileFlows.swipe_on_page('right')
        MobileFlows.featured_products_after_swipe_action()

    @allure.title('Test02: Return to The Previous Page By Click On Element')
    @allure.description('This test verifies that moving to the previous page is successful')
    def test_click_to_return_to_the_previous_page(self):
        MobileFlows.click_to_return_to_the_previous_page()

    @allure.title('Test03: Add Items To The Shopping Cart')
    @allure.description('This test verifies that items were successfully added to the shopping cart')
    def test_verify_electronics_items_count(self):
        MobileFlows.verify_element_before_adding_to_shopping_cart_nikon_d5500_dslr()
        MobileFlows.swipe_on_page('up')
        MobileFlows.verify_item_in_shopping_cart()

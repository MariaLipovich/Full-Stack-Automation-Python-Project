import time

import allure

import page_objects.web_objects_atidstore.store_atidstore
import utilities.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common import get_data, wait, read_csv


class AtidStoreWebFlows:

    @staticmethod
    @allure.step('Return to the store page')
    def store_page():
        UiActions.click_element(page.main_page_atidstore.get_store_atidstore())

    @staticmethod
    @allure.step('Verify main page')
    def verify_main_page():
        elements = [page.main_page_atidstore.get_home_atidstore(), page.main_page_atidstore.get_store_atidstore(),
                    page.main_page_atidstore.get_men_atidstore(), page.main_page_atidstore.get_women_atidstoree(),
                    page.main_page_atidstore.get_accessories_atidstore(), page.main_page_atidstore.get_about_atidstore()]
        Verifications.smart_assert_elements(elements)
        time.sleep(int(get_data('Wait')))
        actual = 'ATID Demo Store'
        Verifications.verify_equals(actual, page.main_page_atidstore.get_atid_demo_store().text)

    @staticmethod
    @allure.step('Verify store page')
    def verify_store():
        UiActions.click_element(page.main_page_atidstore.get_shop_now_atidstore())
        wait("element_is_displayed", page_objects.web_objects_atidstore.store_atidstore.filter_atidstore)
        Verifications.verify_element_with_smart_assertion(page.store_atidstore.get_filter_atidstore())
        time.sleep(3)

    @staticmethod
    @allure.step('Count the number of items on the page')
    def count_items():
        actual = '12'
        expected = len(page.store_atidstore.get_items_atidstore())
        Verifications.verify_equals(actual, str(expected))

    @staticmethod
    @allure.step('Add the items on the Shopping cart')
    def add_item(num_item):
        UiActions.click_element(page.store_atidstore.get_item_atidstore()[num_item - 1])
        UiActions.click_element(page.item_atidstore.get_add_to_cart_atidstore())
        time.sleep(3)

    @staticmethod
    @allure.step('Verify the items on the Shopping cart')
    def verify_count_items(actual_result):
        Verifications.verify_equals(actual_result, page.item_atidstore.get_count_items_atidstore().text)
        time.sleep(int(get_data('Wait')))

    @staticmethod
    @allure.step('Verify the checkout page')
    def checkout_page():
        elem1 = page.item_atidstore.get_before_view_cart_atidstore()
        elem2 = page.item_atidstore.get_checkout_button_atidstore()
        elem1 = elem1.wrapped_element
        elem2 = elem2.wrapped_element
        UiActions.mouse_hover(elem1, elem2)
        time.sleep(int(get_data('Wait')))
        Verifications.verify_element_with_smart_assertion(page.checkout_atidstore.get_checkout_atidstore_title())

    @staticmethod
    @allure.step('login the returning customer')
    def login():
        UiActions.click_element(page.checkout_atidstore.get_login_atidstore())

    @staticmethod
    @allure.step('login the returning customer')
    def login_button_atidstore():
        UiActions.click_element(page.checkout_atidstore.get_login_atidstore_button())

    @staticmethod
    @allure.step('Input username or email data for login')
    def input_csv_username_or_email_data(email: str):
        UiActions.fill_field(page.checkout_atidstore.get_username_atidstore(), email)

    @staticmethod
    @allure.step('Input password data for login')
    def input_csv_password_data(password: str):
        UiActions.fill_field(page.checkout_atidstore.get_password_atidstore(), password)

    @staticmethod
    @allure.step('Input error_message data for login')
    def verify_expected_message(error_message):
        time.sleep(int(get_data('Wait')))
        if error_message == "Username is required.":
            Verifications.verify_equals(page.checkout_atidstore.get_username_is_required_message().text, error_message)
        # elif error_message == "The username " + page.checkout_atidstore.get_username_is_not_registered_message_part2().text + " is not registered on this site. If you are unsure of your username, try your email address instead. ":
        #     common_message = (page.checkout_atidstore.get_username_is_not_registered_message_part1().text +
        #                       page.checkout_atidstore.get_username_is_not_registered_message_part2().text +
        #                       page.checkout_atidstore.get_username_is_not_registered_message_part3().text)
        #     cm = " ".join(common_message)
        #     Verifications.verify_equals(cm, error_message)
        elif error_message == "Unknown email address. Check again or try your username.":
            Verifications.verify_equals(page.checkout_atidstore.get_unknown_email_message().text,
                                        error_message)

    data = read_csv(get_data('CSV_Location_Atid'))





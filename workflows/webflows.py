import time

import allure
import page_objects.web_objects.products_menu_page
import page_objects.web_objects.main_page
import page_objects.web_objects.computers_menu
import page_objects.web_objects.main_page_upper_menu
import utilities.manage_pages as page
from extensions.ui_actions import UiActions
from utilities.common import wait, get_data, read_csv
from extensions.verifications import Verifications


class Webflows:


    @staticmethod
    @allure.step('Verify nopcommerce main page title')
    def verify_main_page():
        wait("element_is_available", page_objects.web_objects.main_page.page_logo)
        Verifications.verify_element_is_displayed(page.web_main_page.main_page())

    @staticmethod
    @allure.step('Verify the elements of the main page menu')
    def verify_main_page_menu():
        elements_list = [page.web_main_page_upper_menu.get_register(), page.web_main_page_upper_menu.get_log_in(),
                         page.web_main_page_upper_menu.get_currency_dropdown(), page.web_main_page_upper_menu.get_wishlist(),
                         page.web_main_page_upper_menu.get_shopping_cart_button()]
        Verifications.soft_displayed(elements_list)

    @staticmethod
    @allure.step('Verify the elements of the main page menu')
    def verify_main_page_menu_with_smart_assert():
        elements_list = [page.web_main_page_upper_menu.get_register(), page.web_main_page_upper_menu.get_log_in(),
                         page.web_main_page_upper_menu.get_currency_dropdown(),
                         page.web_main_page_upper_menu.get_wishlist(),
                         page.web_main_page_upper_menu.get_shopping_cart_button()]
        Verifications.smart_assert_elements(elements_list)

    @staticmethod
    @allure.step('Verify the items of the main page menu')
    def verify_products_menu_page():
        elements_list = [page.web_products_menu.get_computers(), page.web_products_menu.get_electronics(),
                         page.web_products_menu.get_apparel(), page.web_products_menu.get_digital_downloads(),
                         page.web_products_menu.get_books(), page.web_products_menu.get_books.get_jewerly(),
                         page.web_products_menu.get_gift_cards()]
        Verifications.soft_displayed(elements_list)

    @staticmethod
    @allure.step('Mouse over from Computers to Notebooks')
    def verify_notebooks():
        Verifications.verify_element_with_smart_assertion(page.web_main_page.main_page())
        elem1 = page.web_products_menu.get_computers()
        elem2 = page.web_computers_menu.get_notebooks()
        elem1 = elem1.wrapped_element
        elem2 = elem2.wrapped_element
        UiActions.mouse_hover(elem1, elem2)
        time.sleep(int(get_data('Wait')))
    @staticmethod
    @allure.step('Choose items from the Notebooks section')
    def adding_notebook_to_shopping_cart(element_index):
        Verifications.verify_element_with_smart_assertion(page.web_notebooks.get_title())
        UiActions.click_element(page.web_notebooks.get_element_button(element_index))
        Verifications.verify_element_is_displayed(page.web_notebooks.get_adding_item_message())
        time.sleep(int(get_data('Wait')))
    @staticmethod
    @allure.step('Verify the item count in the Shopping Cart after adding')
    def shopping_cart_with_items(expected_count):
        UiActions.click_element(page.web_notebooks.get_shopping_cart_link())
        time.sleep(int(get_data('Wait')))
        Verifications.verify_element_with_smart_assertion(page.web_shopping_cart.page_title())
        actual_count = page.web_shopping_cart.item_count_in_shopping_cart()
        Verifications.verify_count_elements(expected_count, actual_count)

    @staticmethod
    @allure.step('Remove the items from the shopping cart')
    def item_in_shopping_cart(index):
        time.sleep(int(get_data('Wait')))
        UiActions.click_element(page.web_shopping_cart.remove_item_from_shopping_cart()[index])

    @staticmethod
    @allure.step('Verify the item count in the Shopping cart after removing')
    def items_count(expected_count):
        actual_count = page.web_shopping_cart.item_count_in_shopping_cart()
        Verifications.verify_count_elements(expected_count, actual_count)

    @staticmethod
    @allure.step('Click on "Agree with the terms of service" and continue to the checkout process')
    def actions_after_choosing_items():
        UiActions.arrow_down(Verifications.verify_element_is_displayed(page.web_shopping_cart.get_checkbox_button()))
        UiActions.click_element(page.web_shopping_cart.get_checkbox_button())
        UiActions.click_element(page.web_shopping_cart.get_checkout_button())

    @staticmethod
    @allure.step('Input email data for login')
    def input_csv_email_data(email:str):
        UiActions.fill_field(page.web_log_in_page.get_email(), email)

    @staticmethod
    @allure.step('Input password data for login')
    def input_csv_password_data(password:str):
        UiActions.fill_field(page.web_log_in_page.password(), password)

    @staticmethod
    @allure.step('Input error_message data for login')
    def verify_expected_message(error_message):
        time.sleep(int(get_data('Wait')))
        if error_message == "Please enter your email":
            Verifications.verify_equals(page.web_log_in_page.error_message().text, error_message)
        elif error_message == "Please enter a valid email address.":
            Verifications.verify_equals(page.web_log_in_page.error_message_invalid_email().text, error_message)
        elif error_message == "Login was unsuccessful. Please correct the errors and try again.No customer account found":
            Verifications.verify_equals(page.web_log_in_page.error_message_for_unregistered_user().text,
                                                            error_message)

    @staticmethod
    @allure.step('Submit login')
    def log_in_submit():
        time.sleep(int(get_data('Wait')))
        UiActions.click_element(page.web_log_in_page.get_checkbox_remember_me())
        UiActions.click_element(page.web_log_in_page.get_button_log_in())

    @staticmethod
    @allure.step('Filling fields to register a user.')
    def register_valid_user():
        UiActions.click_element(page.web_log_in_page.get_register_button_for_checkout())
        UiActions.click_element(page.web_register_page.gender_female())
        UiActions.fill_field(page.web_register_page.first_name(), "Lea")
        UiActions.fill_field(page.web_register_page.last_name_field(), "Reo")
        UiActions.fill_field(page.web_register_page.register_email(),"user33127@outlook.com")
        UiActions.fill_field(page.web_register_page.password(), "984bf6xb")
        UiActions.fill_field(page.web_register_page.confirm_password(), "984bf6xb")
        UiActions.click_element(page.web_register_page.submit_button())

    @staticmethod
    @allure.step('Verify the Shopping cart page')
    # click on the "Shopping cart" button and open shopping cart page
    # expected = "Shopping cart"
    def from_main_page_to_shopping_cart(expected: str):
        UiActions.click_element(page.web_main_page_upper_menu.get_shopping_cart_button())
        actual = page.web_shopping_cart.page_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Verify that the Shopping cart is empty')
    def verify_empty_shopping_cart_message():
        time.sleep(int(get_data('Wait')))
        Verifications.verify_element_is_displayed(page.web_shopping_cart.get_empty_shopping_cart_message())

    @staticmethod
    @allure.step('Verify Nopcommerce main page')
    def main_page(self):
        self.driver.get(get_data("UrlTesting"))
        time.sleep(int(get_data('Wait')))


    data = read_csv(get_data('CSV_Location'))
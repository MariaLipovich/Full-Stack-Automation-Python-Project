import time

import allure
import self

from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications
from test_cases import conftest
from utilities import manage_pages
from utilities.common import get_data


class MobileFlows:

    @staticmethod
    @allure.step('"Popular categories menu" verification on the home page')
    def popular_categories():
        popular_categories_list = [manage_pages.mobile_home_page.get_electronics_m(),
                                   manage_pages.mobile_home_page.get_apparel_m(), manage_pages.mobile_home_page.get_digital_downloads_m()]
        Verifications.smart_assert_elements(popular_categories_list)

    @staticmethod
    @allure.step('"featured_products menu" verification on the home page')
    def featured_products():
        featured_products_list = [manage_pages.mobile_home_page.get_own_computer_m(),
                                  manage_pages.mobile_home_page.get_macBook_m()]
        Verifications.smart_assert_elements(featured_products_list)

    @staticmethod
    @allure.step('The common method for using the swipe action.')
    def swipe_on_page(diraction):
        width = conftest.mobile_size['width']
        height = conftest.mobile_size['height']
        start_x = None
        start_y = None
        end_x = None
        end_y = None
        if diraction.lower() == 'left':
            start_x = width * 0.1
            start_y = height * 0.5
            end_x = width * 0.9
            end_y = height * 0.5
        elif diraction.lower() == 'right':
            start_x = width * 0.9
            start_y = height * 0.5
            end_x = width * 0.1
            end_y = height * 0.5
        elif diraction.lower() == 'down':
            start_x = width * 0.5
            start_y = height * 0.1
            end_x = width * 0.5
            end_y = height * 0.9
        elif diraction.lower() == 'up':
            start_x = width * 0.5
            start_y = height * 1
            end_x = width * 0.5
            end_y = height * 0
        MobileActions.swipe_action(start_x, start_y, end_x, end_y, int(get_data('SwipeDuration')))

    @staticmethod
    @allure.step('"featured_products menu" verification on the home page after swipe action')
    def featured_products_after_swipe_action():
        featured_products_list_after_swipe = [manage_pages.mobile_home_page.get_htc_smartphone_m(),
                                              manage_pages.mobile_home_page.get_virtual_gift_card_m()]
        Verifications.smart_assert_elements(featured_products_list_after_swipe)

    @staticmethod
    @allure.step('After each test, return to the home page')
    def home_page():
        MobileActions.tap_action(manage_pages.mobile_home_page.get_home_button_m(), 1)

    @staticmethod
    @allure.step('Returning to the previous page')
    def click_to_return_to_the_previous_page():
        element = manage_pages.mobile_home_page.get_electronics_m()
        MobileActions.tap_action(element, 1)
        Verifications.verify_element_with_smart_assertion(manage_pages.mobile_electronics_page.get_electronic_title())
        MobileActions.tap_action(manage_pages.mobile_electronics_page.get_back_button(), 1)
        Verifications.verify_element_with_smart_assertion(manage_pages.mobile_catalog_page.get_catalog_title())

    @staticmethod
    @allure.step('Verify electronics Item')
    def verify_element_before_adding_to_shopping_cart_nikon_d5500_dslr():
        MobileActions.tap_action(manage_pages.mobile_catalog_page.get_catalog_button(), 1)
        MobileActions.tap_action(manage_pages.mobile_catalog_page.get_electronics_button(), 1)
        Verifications.verify_element_with_smart_assertion(manage_pages.mobile_electronics_page.get_electronic_title())
        MobileActions.tap_action(manage_pages.mobile_electronics_page.get_camera_and_photo(), 1)
        MobileActions.tap_action(manage_pages.mobile_electronics_page.get_nikon_d5500_dslr(), 1)
        time.sleep(3)

    @staticmethod
    @allure.step('Add and verify item in the Shopping cart')
    def verify_item_in_shopping_cart():
        MobileActions.tap_action(manage_pages.mobile_electronics_page.get_add_to_cart(), 1)
        MobileActions.tap_action(manage_pages.mobile_shopping_cart.get_shopping_cart_m(), 1)
        Verifications.verify_element_is_displayed(manage_pages.mobile_shopping_cart.shopping_cart_title())
        Verifications.verify_element_with_smart_assertion(manage_pages.mobile_electronics_page.get_nikon_d5500_dslr_black())















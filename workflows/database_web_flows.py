import time

import allure



from extensions.database_extensions import DatabaseExtensions
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
import utilities.manage_pages as page



class DatabaseWebFlows:
    @staticmethod
    @allure.step('Verify page to filling a correct data')
    def verify_iron_man_page():
        time.sleep(3)
        Verifications.verify_element_with_smart_assertion(page.main_page_avengers.get_title())
        UiActions.click_element(page.main_page_avengers.get_iron_man())
        time.sleep(3)
        Verifications.verify_element_is_displayed(page.iron_man_page.get_iron_man_picture())

    @staticmethod
    @allure.step('Verify a correct filled data')
    def fill_data():
        col_names = ['Username', 'Password']
        result = DatabaseExtensions.get_data(col_names, 'Users', 'Username', 'IRONMAN')
        UiActions.fill_field(page.iron_man_page.get_iron_man_username(), result[0][0])
        UiActions.fill_field(page.iron_man_page.get_iron_man_password(), result[0][1])
        UiActions.click_element(page.iron_man_page.get_show_me_iron_man())
        actual = "Iron Man"
        Verifications.verify_equals(actual, page.iron_man_page.get_result_iron_man().text)
#build SQL table












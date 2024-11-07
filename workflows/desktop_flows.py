import time

import allure

from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities import manage_pages as calculator_page


class DesktopFlows:

    @staticmethod
    @allure.step('Change a calculator type and verify that a header is "Time"')
    def change_calculator_type(expected):
        UiActions.click_element(calculator_page.clock_calculator_page.get_calculators_menu())
        UiActions.click_element(calculator_page.clock_calculator_page.get_calculator_type())
        actual = calculator_page.clock_calculator_page.get_calculator_header().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Select unit of measurement top line and verify it')
    def unit_of_measurement_upper(measurement):
        actual = calculator_page.clock_calculator_page.get_choose_upper_unit_measurement()
        UiActions.click_element(actual)
        UiActions.click_element(calculator_page.clock_calculator_page.get_hours())
        Verifications.verify_equals(actual.text, measurement)

    @staticmethod
    @allure.step('Select unit of measurement bottom line and verify it')
    def unit_of_measurement_lower(measurement):
        actual = calculator_page.clock_calculator_page.get_choose_lower_unit_measurement()
        UiActions.click_element(actual)
        UiActions.click_element(calculator_page.clock_calculator_page.get_minutes())
        Verifications.verify_equals(actual.text, measurement)

    @staticmethod
    @allure.step('Return a number')
    def calculate(number):
        if number == '0':
            UiActions.click_element(calculator_page.clock_calculator_page.get_zero())
        elif number == '1':
            UiActions.click_element(calculator_page.clock_calculator_page.get_one())
        elif number == '2':
            UiActions.click_element(calculator_page.clock_calculator_page.get_two())
        elif number == '3':
            UiActions.click_element(calculator_page.clock_calculator_page.get_three())
        elif number == '4':
            UiActions.click_element(calculator_page.clock_calculator_page.get_four())
        elif number == '5':
            UiActions.click_element(calculator_page.clock_calculator_page.get_five())
        elif number == '6':
            UiActions.click_element(calculator_page.clock_calculator_page.get_six())
        elif number == '7':
            UiActions.click_element(calculator_page.clock_calculator_page.get_seven())
        elif number == '8':
            UiActions.click_element(calculator_page.clock_calculator_page.get_eight())
        elif number == '9':
            UiActions.click_element(calculator_page.clock_calculator_page.get_nine())
        else:
            raise Exception("Wrong input. Please, try again")

    @staticmethod
    @allure.step('Get number and calculate according to the selected categories')
    def get_numbers(numbers):
        UiActions.click_element(calculator_page.clock_calculator_page.get_value_1())
        for x in numbers:
            DesktopFlows.calculate(x)

    @staticmethod
    @allure.step('Verify result')
    def verify_result(expected):
        actual = calculator_page.clock_calculator_page.get_value_2().text
        actual = actual.split(" ")
        Verifications.verify_equals(actual[2], expected)

    @staticmethod
    @allure.step('Clear result')
    def clear_result(expected):
        UiActions.click_element(calculator_page.clock_calculator_page.get_clear())
        actual = calculator_page.clock_calculator_page.get_value_2().text
        actual = actual.split(" ")
        Verifications.verify_equals(actual[2], expected)













    

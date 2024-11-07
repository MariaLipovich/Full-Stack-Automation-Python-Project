import time

import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import page_objects.electron_objects.electron_main_page
import utilities
from test_cases.conftest import driver
from utilities import manage_pages as page_electron
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from utilities.common import get_data, wait


class ElectronFlows:

    @staticmethod
    @allure.step("Today`s date")
    def verify_date(expected:str):
        actual = page_electron.electron_main_page_tests.get_task_date()
        Verifications.verify_equals(expected, actual.text)

    @staticmethod
    @allure.step("Create new task")
    def create_task(task):
        UiActions.fill_field(page_electron.electron_main_page_tests.get_create_task(), task)
        UiActions.fill_field(page_electron.electron_main_page_tests.get_create_task(), Keys.ENTER)

    @staticmethod
    @allure.step("Click on date")
    def click_date():
        wait("element_is_available", page_objects.electron_objects.electron_main_page.task_date)
        UiActions.click_element(page_electron.electron_main_page_tests.get_task_date())
        time.sleep(5)

    @staticmethod
    @allure.step("Verify task")
    def verify_tasks(expected):
        time.sleep(3)
        actual = page_electron.electron_main_page_tests.get_task_field()
        Verifications.verify_count_elements(expected, actual)

    @staticmethod
    @allure.step("Complete task")
    def completing_task(number):
        UiActions.mouse_hover_app(page_electron.electron_main_page_tests.get_completing_task()[number])


    @staticmethod
    @allure.step("Click on 'toggle all completed'")
    def click_on_all_completed():
        UiActions.click_element(page_electron.electron_main_page_tests.get_toggle_all_completed())

    @staticmethod
    @allure.step("Verify completed tasks")
    def verify_all_remaining_tasks(expected):
        UiActions.click_element(page_electron.electron_main_page_tests.get_panel())
        time.sleep(3)
        actual = page_electron.electron_main_page_tests.get_remaining_tasks().text
        actual = actual[0]
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step("Get count of active tasks")
    def get_all_tasks():
        tasks = len(page_electron.electron_main_page_tests.get_task_field())
        return tasks

    @staticmethod
    @allure.step("Verify completed tasks")
    def click_on_delete_tasks():
        for x in range(ElectronFlows.get_all_tasks()):
            time.sleep(3)
            UiActions.mouse_hover_app(page_electron.electron_main_page_tests.get_delete_task()[0])











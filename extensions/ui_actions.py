import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest as conf_test


class UiActions:
    @staticmethod
    @allure.step('Click on element')
    def click_element(elem:WebElement):
        elem.click()

    @staticmethod
    @allure.step('Clear text field in element')
    def clear_action(elem:WebElement):
        elem.clear()

    @staticmethod
    @allure.step('Update text')
    def fill_field(elem:WebElement, value:str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('Mouse over two elements')
    def mouse_hover(elem1, elem2):
        conf_test.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Right click on element')
    def mouse_right_click(elem:WebElement):
        conf_test.action.context_click(elem).perform()

    @staticmethod
    @allure.step('Drag and Drop')
    def drag_and_drop(elem1:WebElement, elem2:WebElement):
        conf_test.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step('Arrow down')
    def arrow_down(elem:WebElement):
        conf_test.action.context_click(elem).send_keys(Keys.ARROW_DOWN)

    @staticmethod
    @allure.step('Mouse hover')
    def mouse_hover_app(elem: WebElement):
        ActionChains(conf_test.driver).move_to_element(elem).click().perform()
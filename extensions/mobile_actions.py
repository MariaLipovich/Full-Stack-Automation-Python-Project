import allure

from extensions.ui_actions import UiActions
import test_cases.conftest as conftest


class MobileActions(UiActions):
    @staticmethod
    @allure.step("Tap on element")
    def tap_action(element, times):
        conftest.action.tap(element, times).perform()

    @staticmethod
    @allure.step('Swipe Screen')
    def swipe_action(start_x, start_y, end_x, end_y, duration):
        conftest.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    @allure.step('Zoom on element')
    def zoom_action(element, pixels= 300):
        action1 = conftest.action
        action2 = conftest.action2
        action3 = conftest.action3
        x_location = element.rect['x']
        y_location = element.rect['y']
        action1.long_press(x=x_location, y=y_location).move_to(x=x_location, y=y_location + pixels).wait(500).release()
        action2.long_press(x=x_location, y=y_location).move_to(x=x_location, y=y_location - pixels).wait(500).release()
        action3.add(action1, action2)
        action3.perform()

    @staticmethod
    @allure.step('Pinch on element')
    def pinch_action(element, pixels=300):
        action1 = conftest.action
        action2 = conftest.action2
        action3 = conftest.action3
        x_location = element.rect['x']
        y_location = element.rect['y']
        action1.long_press(x=x_location, y=y_location + pixels).move_to(x=x_location, y=y_location).wait(500).release()
        action2.long_press(x=x_location, y=y_location + pixels).move_to(x=x_location, y=y_location).wait(500).release()
        action3.add(action1, action2)
        action3.perform()

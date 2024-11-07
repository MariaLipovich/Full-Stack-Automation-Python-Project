from selenium.webdriver.support.events import AbstractEventListener
import threading
import time


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("Before Navigating to", url)

    def after_navigate_to(self, url, driver):
        print("After Navigating to", url)

    def before_navigate_back(self, driver):
        print("Before Navigating back", driver.current_url)

    def after_navigate_back(self, driver):
        print("After Navigating to", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before Navigating forward", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After Navigating forward", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before Find Element ", value)

    def after_find(self, by, value, driver):
        print("After Find Element ", value)

    def before_change_value_of(self, elem, driver):
        if elem.tag_name == "input":
            print("Before Change Value", elem.get_attribute("value"))
        else:
            print("Before Change Value", elem.text)

    def after_change_value_of(self, elem, driver):
        if elem.tag_name == "input":
            print("After Change Value", elem.get_attribute("value"))
        else:
            print("After Change Value", elem.text)

    def before_click(self, elem, driver):
        EventListener.button_text = elem.get_attribute("value")
        if elem.tag_name == "input":
            print("Before Click", EventListener.button_text)
        else:
            print("Before Click", EventListener.button_text)

    def after_click(self, elem, driver):
        print("After Click", EventListener.button_text)

    def before_move_to(self, element, driver):
        print(f'About to move to {element}')

    def after_move_to(self, element, driver):
        print(f'Moved to {element}')

    def before_execute_script(self, script, driver):
        print("Before Execute Script", script)

    def after_execute_script(self, script, driver):
        print("After Execute Script", script)

    def before_close(self, driver):
        print("Before Closing Tab")

    def after_close(self, driver):
        print("After Closing Tab")

    def before_quit(self, driver):
        print("Before quiting")

    def after_quit(self, driver):
        print("After quiting")

    def on_exception(self, exception, driver):
        print("On Exception: " + str(exception))
















from selenium.webdriver.common.by import By

desktops = (By.CSS_SELECTOR, "a[href='/desktops']")
notebooks = (By.CSS_SELECTOR, "a[href='/notebooks']")
software = (By.CSS_SELECTOR, "a[href='/computers]")


class ComputersMenu:

    def __init__(self, driver):
        self.driver = driver

    def get_desktops(self):
        return self.driver.find_element(desktops[0], desktops[1])

    def get_notebooks(self):
        return self.driver.find_element(notebooks[0], notebooks[1])

    def get_software(self):
        return self.driver.find_element(software[0], software[1])
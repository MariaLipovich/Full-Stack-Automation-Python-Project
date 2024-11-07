from selenium.webdriver.common.by import By

catalog_title = (By.XPATH, "//*[@contentDescription='Catalog']")
catalog_button = (By.XPATH, "//*[@contentDescription='Catalog\nTab 2 of 4']")
electronics_button = (By.XPATH, "//*[@contentDescription='Electronics']")

class CatalogPage:

    def __init__(self, driver):
        self.driver = driver

    def get_catalog_title(self):
        return self.driver.find_element(catalog_title[0], catalog_title[1])

    def get_catalog_button(self):
        return self.driver.find_element(catalog_button[0], catalog_button[1])

    def get_electronics_button(self):
        return self.driver.find_element(electronics_button[0], electronics_button[1])

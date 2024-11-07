from selenium.webdriver.common.by import By

search_field = (By.ID, "small-searchterms")
search_button = (By.LINK_TEXT, "Search")
search_title = (By.CSS_SELECTOR, "div[class='page-title']")




class SearchStore:

    def __init__(self, driver):
        self.driver = driver

    def get_search_field(self):
        return self.driver.find_element(search_field[0], search_field[1])

    def get_search_button(self):
        return self.driver.find_element(search_button[0], search_button[1])
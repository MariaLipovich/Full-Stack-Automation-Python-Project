from selenium.webdriver.common.by import By

thor_picture = (By.XPATH, "//img[@src='']")
thor_username = (By.ID, "username")
thor_password = (By.ID, "password")
show_me_thor = (By.ID, "submit")



class ThorPage:
    def __init__(self, driver):
        self.driver = driver

    def get_iron_man_picture(self):
        return self.driver.find_element(thor_picture[0], thor_picture[1])

    def get_iron_man_username(self):
        return self.driver.find_element(thor_username[0], thor_username[1])

    def get_iron_man_password(self):
        return self.driver.find_element(thor_password[0], thor_password[1])

    def get_show_me_iron_man(self):
        return self.driver.find_element(show_me_thor[0], show_me_thor[1])

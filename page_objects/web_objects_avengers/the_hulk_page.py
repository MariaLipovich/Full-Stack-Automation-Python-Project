from selenium.webdriver.common.by import By

the_hulk_picture = (By.XPATH, "//img[@src='']")
the_hulk_username = (By.ID, "username")
the_hulk_password = (By.ID, "password")
show_me_the_hulk = (By.ID, "submit")



class TheHulkPage:
    def __init__(self, driver):
        self.driver = driver

    def get_iron_man_picture(self):
        return self.driver.find_element(the_hulk_picture[0], the_hulk_picture[1])

    def get_iron_man_username(self):
        return self.driver.find_element(the_hulk_username[0], the_hulk_username[1])

    def get_iron_man_password(self):
        return self.driver.find_element(the_hulk_username[0], the_hulk_username[1])

    def get_show_me_iron_man(self):
        return self.driver.find_element(show_me_the_hulk[0], show_me_the_hulk[1])

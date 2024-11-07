from selenium.webdriver.common.by import By

iron_man_picture = (By.XPATH, "//img[@src='../images/ironman.png']")
iron_man_username = (By.ID, "username")
iron_man_password = (By.ID, "password")
show_me_iron_man = (By.ID, "submit")
result_iron_man = (By.CSS_SELECTOR, 'span[class="hero__primary-text"]')



class IronMan:
    def __init__(self, driver):
        self.driver = driver

    def get_iron_man_picture(self):
        return self.driver.find_element(iron_man_picture[0], iron_man_picture[1])

    def get_iron_man_username(self):
        return self.driver.find_element(iron_man_username[0], iron_man_username[1])

    def get_iron_man_password(self):
        return self.driver.find_element(iron_man_password[0], iron_man_password[1])

    def get_show_me_iron_man(self):
        return self.driver.find_element(show_me_iron_man[0], show_me_iron_man[1])

    def get_result_iron_man(self):
        return self.driver.find_element(result_iron_man[0], result_iron_man[1])



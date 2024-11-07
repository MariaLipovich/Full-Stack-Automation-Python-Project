from selenium.webdriver.common.by import By

iron_man_picture = (By.XPATH, "//img[@src='../images/captainamerica.png']")
captain_america_username = (By.ID, "username")
captain_america_password = (By.ID, "password")
show_me_captain_america = (By.ID, "submit")


class CaptainAmerica:
    def __init__(self, driver):
        self.driver = driver

    def get_iron_man_picture(self):
        return self.driver.find_element(iron_man_picture[0], iron_man_picture[1])

    def get_iron_man_username(self):
        return self.driver.find_element(captain_america_username[0], captain_america_username[1])

    def get_iron_man_password(self):
        return self.driver.find_element(captain_america_password[0], captain_america_password[1])

    def get_show_me_captain_america(self):
        return self.driver.find_element(show_me_captain_america[0], show_me_captain_america[1])

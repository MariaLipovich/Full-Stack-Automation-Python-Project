from selenium.webdriver.common.by import By

iron_man = (By.CSS_SELECTOR, "a[href='loginIronMan.html']")
captain_america = (By.CSS_SELECTOR, "a[href='loginCaptainAmerica.html']")
the_hulk = (By.CSS_SELECTOR, "a[href='loginTheHulk.html']")
thor = (By.CSS_SELECTOR, "a[href='loginThor.html']")
title_avengers = (By.XPATH, "//img[@src='../images/avengers.png']")

class MainPageAvengers:

    def __init__(self, driver):
        self.driver = driver

    def get_iron_man(self):
        return self.driver.find_element(iron_man[0], iron_man[1])

    def get_captain_america(self):
        return self.driver.find_element(captain_america[0], captain_america[1])

    def get_the_hulk(self):
        return self.driver.find_element(the_hulk[0], the_hulk[1])

    def get_thor(self):
        return self.driver.find_element(thor[0], thor[1])

    def get_title(self):
        return self.driver.find_element(title_avengers[0], title_avengers[1])



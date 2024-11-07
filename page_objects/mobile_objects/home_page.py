from selenium.webdriver.common.by import By

home_button = (By.XPATH, "//*[@contentDescription='Home\nTab 1 of 4']")
electronics = (By.XPATH, "//*[@contentDescription='Electronics']")
apparel = (By.XPATH, "//*[@contentDescription='Apparel']")
digital_downloads = (By.XPATH, "//*[@contentDescription='Digital downloads']")
own_computer = (By.XPATH, "//*[@contentDescription='new\nBuild your own computer\n5.0\n$1,200.00']")
apple_macBook = (By.XPATH, "//*[@contentDescription='Apple MacBook Pro\n5.0\n$1,800.00']")
htc_smartphone = (By.XPATH, "//*[@contentDescription='new\nHTC smartphone\n4.0\n$245.00']")
virtual_gift_card = (By.XPATH, "//*[@contentDescription='$25 Virtual Gift Card\n5.0\n$25.00']")



class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_home_button_m(self):
        return self.driver.find_element(home_button[0], home_button[1])

    def get_electronics_m(self):
        return self.driver.find_element(electronics[0], electronics[1])

    def get_apparel_m(self):
        return self.driver.find_element(apparel[0], apparel[1])

    def get_digital_downloads_m(self):
        return self.driver.find_element(digital_downloads[0], digital_downloads[1])

    def get_own_computer_m(self):
        return self.driver.find_element(own_computer[0], own_computer[1])

    def get_macBook_m(self):
        return self.driver.find_element(apple_macBook[0], apple_macBook[1])

    def get_htc_smartphone_m(self):
        return self.driver.find_element(htc_smartphone[0], htc_smartphone[1])

    def get_virtual_gift_card_m(self):
        return self.driver.find_element(virtual_gift_card[0], virtual_gift_card[1])




from selenium.webdriver.common.by import By

computers = (By.CSS_SELECTOR, "a[href='/computers']")
# computers = (By.PARTIAL_LINK_TEXT, "Computers")
electronics = (By.LINK_TEXT, "Electronics")
apparel = (By.LINK_TEXT, "Apparel")
digital_downloads = (By.LINK_TEXT, "Digital downloads")
books = (By.LINK_TEXT, "Books")
jewelry = (By.LINK_TEXT, "Jewelry")
gift_cards = (By.LINK_TEXT, "Gift Cards")



class ProductsMenuPage:


    def __init__(self, driver):
        self.driver = driver

    def get_computers(self):
        return self.driver.find_element(computers[0], computers[1])

    def get_electronics(self):
        return self.driver.find_element(electronics[0], electronics[1])

    def get_apparel(self):
        return self.driver.find_element(apparel[0], apparel[1])

    def get_digital_downloads(self):
        return self.driver.find_element(digital_downloads[0], digital_downloads[1])

    def get_books(self):
        return self.driver.find_element(books[0], books[1])

    def get_jewerly(self):
        return self.driver.find_element(jewelry[0], jewelry[1])


    def get_gift_cards(self):
        return self.driver.find_element(gift_cards[0], gift_cards[1])








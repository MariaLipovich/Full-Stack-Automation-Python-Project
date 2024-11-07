from selenium.webdriver.common.by import By

shopping_cart = (By.ID, "topcartlink")
register = (By.LINK_TEXT, "Register")
log_in = (By.CLASS_NAME, "ico-login")
wishlist = (By.LINK_TEXT, "Wishlist")
currency = (By.ID, "customerCurrency")

class MainPageUpperMenu:

    def __init__(self, driver):
        self.driver = driver

    def get_register(self):
        return self.driver.find_element(register[0], register[1])

    def get_log_in(self):
        return self.driver.find_element(log_in[0], log_in[1])

    def get_currency_dropdown(self):
        return self.driver.find_element(currency[0], currency[1])

    def get_wishlist(self):
        return self.driver.find_element(wishlist[0], wishlist[1])

    def get_shopping_cart_button(self):
        return self.driver.find_element(shopping_cart[0], shopping_cart[1])
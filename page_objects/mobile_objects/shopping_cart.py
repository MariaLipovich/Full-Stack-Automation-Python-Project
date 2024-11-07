from selenium.webdriver.common.by import By

shopping_cart_button = (By.XPATH, "//*[@contentDescription='1\nCart\nTab 3 of 4']")
shopping_cart_title = (By.XPATH, "//*[@contentDescription='Shopping Cart']")
forgot_password = (By.XPATH, "//*[@contentDescription='Forgot password?']")

class ShoppingCartM:

    def __init__(self, driver):
        self.driver = driver

    def get_shopping_cart_m(self):
        return self.driver.find_element(shopping_cart_button[0], shopping_cart_button[1])

    def shopping_cart_title(self):
        return self.driver.find_element(shopping_cart_title[0], shopping_cart_title[1])


    def get_forgot_password_m(self):
        return self.driver.find_element(forgot_password[0], forgot_password[1])


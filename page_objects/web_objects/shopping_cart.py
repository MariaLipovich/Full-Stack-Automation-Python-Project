from selenium.webdriver.common.by import By

shopping_cart_title = (By.CSS_SELECTOR, "div[class='page-title']")
empty_shopping_cart_message = (By.CSS_SELECTOR, "div[class='no-data']")
item_in_shopping_cart = (By.CSS_SELECTOR, "div[class='table-wrapper']")
remove_item = (By.CSS_SELECTOR, "td[class='remove-from-cart']")
item_count = (By.XPATH, "//*[@id='shopping-cart-form']/div[1]/table/tbody/tr")
checkout_button = (By.ID, "checkout")
checkbox_button = (By.ID, "termsofservice")

class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        return self.driver.find_element(shopping_cart_title[0], shopping_cart_title[1])

    def get_empty_shopping_cart_message(self):
        return self.driver.find_element(empty_shopping_cart_message[0], empty_shopping_cart_message[1])

    def get_item_in_shopping_cart(self, element_index):
        return self.driver.find_elements(item_in_shopping_cart[0], item_in_shopping_cart[1])[element_index]

    def remove_item_from_shopping_cart(self):
        return self.driver.find_elements(remove_item[0], remove_item[1])

    def item_count_in_shopping_cart(self):
        return self.driver.find_elements(item_count[0], item_count[1])

    def get_checkout_button(self):
        return self.driver.find_element(checkout_button[0], checkout_button[1])

    def get_checkbox_button(self):
        return self.driver.find_element(checkbox_button[0], checkbox_button[1])






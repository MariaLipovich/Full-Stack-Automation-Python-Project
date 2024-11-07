from selenium.webdriver.common.by import By

notebooks = (By.LINK_TEXT, "Notebooks")
element_button = (By.CSS_SELECTOR, "button[class='button-2 product-box-add-to-cart-button']")
adding_item_message = (By.CSS_SELECTOR, "p[class='content']")
shopping_cart_link = (By.CSS_SELECTOR, "a[href='/cart']")



class Notebooks:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(notebooks[0], notebooks[1])

    def get_element_button(self, element_index):
        return self.driver.find_elements(element_button[0], element_button[1])[element_index]

    def get_adding_item_message(self):
        return self.driver.find_element(adding_item_message[0], adding_item_message[1])

    def get_shopping_cart_link(self):
        return self.driver.find_element(shopping_cart_link[0], shopping_cart_link[1])




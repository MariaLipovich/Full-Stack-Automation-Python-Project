from selenium.webdriver.common.by import By

add_to_cart_atidstore = (By.NAME, "add-to-cart")
count_items_atidstore = (By.CSS_SELECTOR, "span[class='count']")
view_cart_atidstore = (By.CSS_SELECTOR, "a[href='https://atid.store/cart-2/']")
before_view_cart_atidstore = (By.CSS_SELECTOR, "span[class='count']")
checkout_button_atidstore = (By.CSS_SELECTOR, "a[href='https://atid.store/checkout-2/']")


class ItemAtidStore:
    def __init__(self, driver):
        self.driver = driver

    def get_add_to_cart_atidstore(self):
        return self.driver.find_element(add_to_cart_atidstore[0], add_to_cart_atidstore[1])

    def get_count_items_atidstore(self):
        return self.driver.find_element(count_items_atidstore[0], count_items_atidstore[1])

    def get_view_cart_atidstore(self):
        return self.driver.find_elements(view_cart_atidstore[0], view_cart_atidstore[1])[0]

    def get_before_view_cart_atidstore(self):
        return self.driver.find_element(before_view_cart_atidstore[0], before_view_cart_atidstore[1])

    def get_checkout_button_atidstore(self):
        return self.driver.find_element(checkout_button_atidstore[0], checkout_button_atidstore[1])

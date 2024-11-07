from selenium.webdriver.common.by import By

checkout_atidstore_title = (By.CSS_SELECTOR, "h1[class='elementor-heading-title elementor-size-default']")
login_atidstore = (By.CLASS_NAME, "showlogin")
login_atidstore_button = (By.NAME, "login")
username_atidstore = (By.ID, "username")
password_atidstore = (By.ID, "password")
username_is_required_message = (By.XPATH, "//li/strong/following-sibling::text()")
unknown_email_message = (By.XPATH, "//ul[@class='woocommerce-error']//li")
username_is_not_registered_message_part1 = (By.XPATH, "//li/strong/following-sibling::text()")
username_is_not_registered_message_part2 = (By.XPATH, "//li/strong[last()]")
username_is_not_registered_message_part3 = (By.XPATH, "//li/strong[last()]/following-sibling::text()")




class CheckoutAtidStore:
    def __init__(self, driver):
        self.driver = driver

    def get_checkout_atidstore_title(self):
        return self.driver.find_element(checkout_atidstore_title[0], checkout_atidstore_title[1])

    def get_login_atidstore(self):
        return self.driver.find_element(login_atidstore[0], login_atidstore[1])

    def get_username_atidstore(self):
        return self.driver.find_element(username_atidstore[0], username_atidstore[1])

    def get_password_atidstore(self):
        return self.driver.find_element(password_atidstore[0], password_atidstore[1])

    def get_username_is_required_message(self):
        return self.driver.find_element(username_is_required_message[0], username_is_required_message[1])

    def get_login_atidstore_button(self):
        return self.driver.find_element(login_atidstore_button[0], login_atidstore_button[1])

    def get_unknown_email_message(self):
        return self.driver.find_element(unknown_email_message[0], unknown_email_message[1])

    def get_username_is_not_registered_message_part1(self):
        return self.driver.find_element(username_is_not_registered_message_part1[0], username_is_not_registered_message_part1[1])

    def get_username_is_not_registered_message_part2(self):
        return self.driver.find_element(username_is_not_registered_message_part2[0], username_is_not_registered_message_part2[1])

    def get_username_is_not_registered_message_part3(self):
        return self.driver.find_element(username_is_not_registered_message_part3[0], username_is_not_registered_message_part3[1])






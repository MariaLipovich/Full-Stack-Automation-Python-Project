from selenium.webdriver.common.by import By

email_log_in = (By.CLASS_NAME, "email")
password_log_in = (By.ID, "Password")
button_log_in = (By.CSS_SELECTOR, "button[type='submit']")
checkbox_remember_me = (By.ID, "RememberMe")
register_button = (By.PARTIAL_LINK_TEXT, "Register")
error_message = (By.XPATH, "//span[@id='Email-error']")
error_message_invalid_email = (By.XPATH, "//span[@id='Email-error']")
error_message_for_unregistered_user = (By.XPATH,"//div[@class='message-error validation-summary-errors']")


class LogInPage:
    def __init__(self, driver):
        self.driver = driver

    def get_email(self):
        return self.driver.find_element(email_log_in[0], email_log_in[1])

    def password(self):
        return self.driver.find_element(password_log_in[0], password_log_in[1])

    def get_checkbox_remember_me(self):
        return self.driver.find_element(checkbox_remember_me[0], checkbox_remember_me[1])

    def get_button_log_in(self):
        return self.driver.find_elements(button_log_in[0], button_log_in[1])[1]

    def get_register_button_for_checkout(self):
        return self.driver.find_element(register_button[0], register_button[1])

    def get_error_message(self):
        return self.driver.find_element(error_message[0], error_message[1])

    def get_error_message_for_unregestered_user(self):
        return self.driver.find_element(error_message_for_unregistered_user[0], error_message_for_unregistered_user[1])

    def get_error_message_invalid_email(self):
        return self.driver.find_element(error_message_invalid_email[0], error_message_invalid_email[1])



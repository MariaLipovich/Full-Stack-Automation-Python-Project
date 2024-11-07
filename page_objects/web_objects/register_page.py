from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


select_gender_female = (By.XPATH,"//div[@id='gender-female']")
select_gender_male = (By.XPATH,"//div[@id='gender-male']")
first_name_field = (By.ID, "FirstName")
page_title_register = (By.XPATH, "//div[@class='page-title']")
last_name_field = (By.ID, "LastName")
birthday_field = (By.NAME, "DateOfBirthDay")
birth_month_field = (By.NAME, "DateOfBirthMonth")
birth_year_field = (By.NAME, "DateOfBirthYear")
register_emai_field = (By.NAME, "Email")
company_name = (By.ID, "Company")
newsletter_checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
password_field = (By.NAME, "Password")
confirm_password_field = (By.NAME, "ConfirmPassword")
register_button = (By.CSS_SELECTOR, "button[class='button-1 register-next-step-button']")
valid_message = (By.CSS_SELECTOR, "div[class='result']")

class Register:

    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        return self.driver.find_element(page_title_register[0], page_title_register[1])

    def gender_female(self):
        return self.driver.find_element(select_gender_female[0], select_gender_female[1])

    def gender_male(self):
        return self.driver.find_element(select_gender_male[0], select_gender_male[1])

    def first_name(self):
        return self.driver.find_element(first_name_field[0], first_name_field[1])

    def last_name_field(self):
        return self.driver.find_element(last_name_field[0], last_name_field[1])

    def birth_day(self):
        return self.driver.find_element(birthday_field[0], birthday_field[1])

    def birth_month(self):
        return self.driver.find_element(birth_month_field[0], birth_month_field[1])

    def birth_year(self):
        return self.driver.find_element(birth_year_field[0], birth_year_field[1])

    def register_email(self):
        return self.driver.find_element(register_emai_field[0], register_emai_field[1])

    def company_field(self):
        return self.driver.find_element(company_name[0], company_name[1])

    def newsletter(self):
        return self.driver.find_element(newsletter_checkbox[0], newsletter_checkbox[1])

    def password(self):
        return self.driver.find_element(password_field[0], password_field[1])

    def confirm_password(self):
        return self.driver.find_element(confirm_password_field[0], confirm_password_field[1])

    def submit_button(self):
        return self.driver.find_element(register_button[0], register_button[1])

    def get_valid_message(self):
        return self.driver.find_element(valid_message[0], valid_message[1])





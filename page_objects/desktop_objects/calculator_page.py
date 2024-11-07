from selenium.webdriver.common.by import By

calculators_menu = (By.XPATH, "//*[@AutomationId='TogglePaneButton']")
calculator_type = (By.XPATH, "//*[@AutomationId='Time']")
calculator_header = (By.XPATH, "//*[@AutomationId='Header']")
zero = (By.XPATH, "//*[@AutomationId='num0Button']")
one = (By.XPATH, "//*[@AutomationId='num1Button']")
two = (By.XPATH, "//*[@AutomationId='num2Button']")
three = (By.XPATH, "//*[@AutomationId='num3Button']")
four = (By.XPATH, "//*[@AutomationId='num4Button']")
five = (By.XPATH, "//*[@AutomationId='num5Button']")
six = (By.XPATH, "//*[@AutomationId='num6Button']")
seven = (By.XPATH, "//*[@AutomationId='num7Button']")
eight = (By.XPATH, "//*[@AutomationId='num8Button']")
nine = (By.XPATH, "//*[@AutomationId='num9Button']")
clear = (By.XPATH, "//*[@AutomationId='ClearEntryButtonPos0']")
choose_upper_unit_measurement = (By.XPATH, "//*[@AutomationId='Units1']")
choose_lower_unit_measurement = (By.XPATH, "//*[@AutomationId='Units2']")
hours = (By.NAME, "Hours")
minutes = (By.NAME, "Minutes")
days = (By.NAME, "Days")
seconds = (By.NAME, "Seconds")
weeks = (By.NAME, "Weeks")
years = (By.NAME, "Years")
microseconds = (By.NAME, "Weeks")
milliseconds = (By.NAME, "Milliseconds")
value1 = (By.XPATH, "//*[@AutomationId='Value1']")
value2 = (By.XPATH, "//*[@AutomationId='Value2']")



class ClockCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_calculators_menu(self):
        return self.driver.find_element(calculators_menu[0], calculators_menu[1])

    def get_calculator_type(self):
        return self.driver.find_element(calculator_type[0], calculator_type[1])

    def get_calculator_header(self):
        return self.driver.find_element(calculator_header[0], calculator_header[1])

    def get_zero(self):
        return self.driver.find_element(zero[0], zero[1])

    def get_one(self):
        return self.driver.find_element(one[0], one[1])

    def get_two(self):
        return self.driver.find_element(two[0], two[1])

    def get_three(self):
        return self.driver.find_element(three[0], three[1])

    def get_four(self):
        return self.driver.find_element(four[0], four[1])

    def get_five(self):
        return self.driver.find_element(five[0], five[1])

    def get_six(self):
        return self.driver.find_element(six[0], six[1])

    def get_seven(self):
        return self.driver.find_element(seven[0], seven[1])

    def get_eight(self):
        return self.driver.find_element(eight[0], eight[1])

    def get_nine(self):
        return self.driver.find_element(nine[0], nine[1])

    def get_clear(self):
        return self.driver.find_element(clear[0], clear[1])

    def get_choose_upper_unit_measurement(self):
        return self.driver.find_element(choose_upper_unit_measurement[0], choose_upper_unit_measurement[1])

    def get_choose_lower_unit_measurement(self):
        return self.driver.find_element(choose_lower_unit_measurement[0], choose_lower_unit_measurement[1])

    def get_hours(self):
        return self.driver.find_element(hours[0], hours[1])

    def get_minutes(self):
        return self.driver.find_element(minutes[0], minutes[1])

    def get_days(self):
        return self.driver.find_element(days[0], days[1])

    def get_seconds(self):
        return self.driver.find_element(seconds[0], seconds[1])

    def get_weeks(self):
        return self.driver.find_element(weeks[0], weeks[1])

    def years(self):
        return self.driver.find_element(years[0], years[1])

    def get_microseconds(self):
        return self.driver.find_element(microseconds[0], microseconds[1])

    def get_milliseconds(self):
        return self.driver.find_element(milliseconds[0], milliseconds[1])

    def get_value_1(self):
        return self.driver.find_element(value1[0], value1[1])

    def get_value_2(self):
        return self.driver.find_element(value2[0], value2[1])

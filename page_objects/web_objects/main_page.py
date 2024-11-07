from selenium.webdriver.common.by import By

verify_human_frame = (By.XPATH, "//iframe[@title='Widget containing a Cloudflare security challenge']")
# verify_human_frame = (By.XPATH, "//")
page_logo = (By.XPATH, "//div[@class='header-logo']")
verify_human = (By.XPATH, "//label[@class='cb-i']")

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def main_page(self):
        return self.driver.find_element(page_logo[0], page_logo[1])

    def get_verify_human(self):
        return self.driver.find_element(verify_human[0], verify_human[1])

    def get_verify_human_frame(self):
        return self.driver.find_element(verify_human_frame[0], verify_human_frame[1])






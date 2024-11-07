from selenium.webdriver.common.by import By

back_button = (By.XPATH, "//*[@class='android.widget.Button']")
search_button = (By.XPATH, "//*[@class='android.widget.Button']")
filter_button = (By.XPATH, "//*[@class='android.widget.Button']")
header_page =  (By.XPATH, "//*[@contentDescription='Electronics']")
camera_and_photo = (By.XPATH, "//*[@contentDescription='Camera & photo']")
cell_phones = (By.XPATH, "//*[@contentDescription='Cell phones']")
others = (By.XPATH, "//*[@contentDescription='Others']")
nikon_d5500_dslr = (By.XPATH, "//*[@contentDescription='Nikon D5500 DSLR\n0.0\nFrom\n$630.00']")
nikon_d5500_dslr_black = (By.XPATH, "//*[@contentDescription='Nikon D5500 DSLR - Black\nSKU: N5500DS_B\nPrice: $670.00\n1\n$670.00']")
add_to_cart = (By.XPATH, "//*[@contentDescription='Add to Cart']")

class ELectronicsPageMobile:

    def __init__(self, driver):
        self.driver = driver

    def get_back_button(self):
        return self.driver.find_elements(back_button[0], back_button[1])[0]

    def get_search_button(self):
        return self.driver.find_elements(back_button[0], back_button[1])[1]

    def get_filter_button(self):
        return self.driver.find_elements(filter_button[0], filter_button[1])[2]

    def get_electronic_title(self):
        return self.driver.find_element(header_page[0], header_page[1])

    def get_camera_and_photo(self):
        return self.driver.find_element(camera_and_photo[0], camera_and_photo[1])

    def get_cell_phones(self):
        return self.driver.find_element(cell_phones[0], cell_phones[1])

    def get_others(self):
        return self.driver.find_element(others[0], others[1])

    def get_nikon_d5500_dslr(self):
        return self.driver.find_element(nikon_d5500_dslr[0], nikon_d5500_dslr[1])

    def get_add_to_cart(self):
        return self.driver.find_element(add_to_cart[0], add_to_cart[1])

    def get_nikon_d5500_dslr_black(self):
        return self.driver.find_element(nikon_d5500_dslr_black[0], nikon_d5500_dslr_black[1])




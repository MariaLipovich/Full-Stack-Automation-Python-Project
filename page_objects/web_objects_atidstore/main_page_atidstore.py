from selenium.webdriver.common.by import By

home_atidstore = (By.ID, 'menu-item-381')
store_atidstore = (By.ID, 'menu-item-45')
men_atidstore = (By.ID, 'menu-item-266')
women_atidstore = (By.ID, 'menu-item-267')
accessories_atidstore = (By.ID, 'menu-item-671')
about_atidstore = (By.ID, "menu-item-828")
shop_now_atidstore = (By.CSS_SELECTOR, "a[href='https://atid.store/store/']")
atid_demo_store = (By.CSS_SELECTOR, "h1[class='elementor-heading-title elementor-size-default']")





class MainPageAtidStore:
    def __init__(self, driver):
        self.driver = driver

    def get_home_atidstore(self):
        return self.driver.find_element(home_atidstore[0], home_atidstore[1])

    def get_store_atidstore(self):
        return self.driver.find_element(store_atidstore[0], store_atidstore[1])

    def get_men_atidstore(self):
        return self.driver.find_element(men_atidstore[0], men_atidstore[1])

    def get_women_atidstoree(self):
        return self.driver.find_element(women_atidstore[0], women_atidstore[1])

    def get_accessories_atidstore(self):
        return self.driver.find_element(accessories_atidstore[0], accessories_atidstore[1])

    def get_about_atidstore(self):
        return self.driver.find_element(about_atidstore[0], about_atidstore[1])

    def get_shop_now_atidstore(self):
        return self.driver.find_element(shop_now_atidstore[0], shop_now_atidstore[1])

    def get_atid_demo_store(self):
        return self.driver.find_element(atid_demo_store[0], atid_demo_store[1])
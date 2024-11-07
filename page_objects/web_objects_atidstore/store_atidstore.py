from selenium.webdriver.common.by import By

filter_atidstore = (By.CSS_SELECTOR, "h2[class='widget-title']")
categories_atidstore = (By.CSS_SELECTOR, "h2[class='widget-title']")
best_cellers_atidstore = (By.CSS_SELECTOR, "h2[class='widget-title']")
item_atidstore = (By.CSS_SELECTOR, "div[class='astra-shop-thumbnail-wrap']")





class StoreAtidStore:
    def __init__(self, driver):
        self.driver = driver

    def get_filter_atidstore(self):
        return self.driver.find_elements(filter_atidstore[0], filter_atidstore[1])[0]

    def get_categories_atidstore(self):
        return self.driver.find_elements(categories_atidstore[0], categories_atidstore[1])[1]

    def get_best_cellers_atidstore(self):
        return self.driver.find_elements(best_cellers_atidstore[0], best_cellers_atidstore[1])[2]

    def get_items_atidstore(self):
        return self.driver.find_elements(item_atidstore[0], item_atidstore[1])

    def get_item_atidstore(self):
        return self.driver.find_elements(item_atidstore[0], item_atidstore[1])
from selenium.webdriver.common.by import By

no_task_messange = (By.CSS_SELECTOR, "div[class='wrapper_DtvJU']")
create_task = (By.CSS_SELECTOR, "input[type='text']")
task_date = (By.CSS_SELECTOR, "span[class='dateFormatted_3GjaR']")
task_color = (By.CSS_SELECTOR, "svg[class='downArrowIcon_3Zu5N']")
task_fields = (By.CSS_SELECTOR, "div[class='taskWrapper_2u8dN']")
task_completing = (By.XPATH, "//div[@class='task_BEG6D task_2vpFW']//*[local-name()='svg']//*[local-name()='circle' and @stroke='#ededed']")
toggle_all_completed = (By.CSS_SELECTOR, "div[class='allCompletedIconWrapper_2rCqr']")
panel = (By.CSS_SELECTOR, "div[class='toggleVisibilityPanel_hNPyc']")
remaining_tasks = (By.CSS_SELECTOR, "span[class='remainingTasks_1ijI7']")
delete_task = (By.CSS_SELECTOR, "svg[class='destroy_19w1q']")



class ElectronMainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_no_task_messange(self):
        return self.driver.find_element(no_task_messange[0], no_task_messange[1])

    def get_create_task(self):
        return self.driver.find_element(create_task[0], create_task[1])

    def get_task_date(self):
        return self.driver.find_element(task_date[0], task_date[1])

    def get_task_color(self):
        return self.driver.find_element(task_color[0], task_color[1])

    def get_task_field(self):
        return self.driver.find_elements(task_fields[0], task_fields[1])

    def get_completing_task(self):
        return self.driver.find_elements(task_completing[0], task_completing[1])

    def get_toggle_all_completed(self):
        return self.driver.find_element(toggle_all_completed[0], toggle_all_completed[1])

    def get_panel(self):
        return self.driver.find_element(panel[0], panel[1])

    def get_remaining_tasks(self):
        return self.driver.find_element(remaining_tasks[0], remaining_tasks[1])

    def get_delete_task(self):
        return self.driver.find_elements(delete_task[0], delete_task[1])








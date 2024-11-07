import csv
import time


from selenium.webdriver.support.wait import WebDriverWait
import test_cases.conftest as conftest
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
import utilities.manage_pages as page


######################################################
# Function name: get_data
# Description: This function reads data from specific file
# Parameters: node_name
# Return: node value
######################################################
def get_data(node_name):
    root = ET.parse(r"C:\development\PythonAtidAutomation\final_project_infrastructure\configuration\data.xml").getroot()
    return root.find(".//" + node_name).text


######################################################
# Function name: wait
# Description: This function pauses actions until the condition is met or the timeout period expires
# Parameters: state_element, element
######################################################
def wait(state_element, element):
    if state_element == "element_is_available":
        WebDriverWait(conftest.driver, int(get_data("Wait"))).until(EC.presence_of_element_located((element[0], element[1])))
    if state_element == "element_is_displayed":
        WebDriverWait(conftest.driver, 10).until(EC.visibility_of_element_located((element[0], element[1])))
    if state_element == "frame to be available":
        WebDriverWait(conftest.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((element[0], element[1])))
    if state_element == "element to be clickable":
        WebDriverWait(conftest.driver, 20).until(EC.element_to_be_clickable((element[0], element[1])))


######################################################
# Function name: read_csv
# Description: This function reads data from csv file and loads its contents into a dataframe
# Parameters: element
# Return: rows of data
######################################################
def read_csv(element):
    rows = []
    data_file = open(element)
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


######################################################
# Function name: get_time
# Description: This function returns the current time
# Return: current time
######################################################
def get_time():
    return time.time()

# additional wait for simple using disribes available and displayed elements
class additional_wait:
    ELEMENT_IS_AVAILABLE = "element_is_available"
    ELEMENT_IS_DISPLAYED = "element_us_displayed"



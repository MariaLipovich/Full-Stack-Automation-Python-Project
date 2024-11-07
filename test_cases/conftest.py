import os

import appium.webdriver
import allure
import mysql.connector
import pytest
# import selenium
import selenium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from applitools.selenium import Eyes
# from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.common import get_data, get_time
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None
action2 = None
action3 = None
mobile_size = None
eyes = Eyes()
connectorDB = None

######################################################
# Function name: _init_web_driver
# Description: This function performs environment preparation for web testing
# Parameters: The browser name
######################################################
@pytest.fixture(scope='class')
def _init_web_driver(request):
    if get_data('ExecuteApplitools') == 'True':
        globals()['driver'] = get_web_driver()
    elif get_data('ExecuteApplitools') == 'False':
        event_driver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(event_driver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('Wait')))
    if get_data('UrlWeb') == "Nopcommerce":
        driver.get(get_data('UrlTesting'))
    elif get_data('UrlWeb') == "Avengers":
        driver.get(get_data('UrlTestingDB'))
    elif get_data('UrlWeb') == "AtidStore":
        driver.get(get_data('UrlTestingAtid'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    if get_data('UrlWeb') == "Nopcommerce":
        ManagePages.init_web_pages()
    elif get_data('UrlWeb') == "Avengers":
        ManagePages.init_web_pages_avengers()
    elif get_data('UrlWeb') == "AtidStore":
        ManagePages.init_web_pages_atidstore()
    if get_data('ExecuteApplitools') == 'True':
        eyes.api_key = get_data('ApplitoolsAPIKey')
    yield
    driver.quit()
    if get_data('ExecuteApplitools') == 'True':
        eyes.close()
        eyes.abort()


######################################################
# Function name: _init_mobile_driver
# Description: This function performs environment preparation for mobile testing
# Parameters: The platform name
######################################################
@pytest.fixture(scope='class')
def _init_mobile_driver(request):
    event_driver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(event_driver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('Wait')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['action3'] = MultiAction(driver)
    request.cls.action3 = globals()['action3']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


######################################################
# Function name: _init_electron_driver
# Description: This function performs environment preparation for electron apps testing
# Parameters: The Electron driver
######################################################
@pytest.fixture(scope='class')
def _init_electron_driver(request):
    event_driver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(event_driver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('Wait')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


######################################################
# Function name: _init_desktop_driver
# Description: This function performs environment preparation for desktop apps testing
# Parameters: The desktop driver
######################################################
@pytest.fixture(scope='class')
def _init_desktop_driver(request):
    event_driver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(event_driver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(get_data('Wait'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_desktop_pages()
    yield
    driver.quit()

######################################################
# Function name: _init_connector_database
# Description: This function performs environment preparation for web testing using database
# Parameters: mysql connector
######################################################
@pytest.fixture(scope='class')
def _init_connector_database(request):
    connectorDB = mysql.connector.connect(
        host = get_data('DatabaseHost'),
        database = get_data('DatabaseName'),
        user = get_data('DatabaseUser'),
        password = get_data('DatabasePassword')
    )
    globals()['connectorDB'] = connectorDB
    request.cls.connector = connectorDB
    yield
    connectorDB.close()

# This function returns a WebDriver instance based on the specified browser.
def get_web_driver():
    web_driver = get_data('BrowserData')
    # web_driver = os.getenv('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()

    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong output, Unrecognised Browser")
    return driver

# This function returns an Appium WebDriver instance configured for mobile automation
def get_mobile_driver():
    if get_data('PlatformName').lower() == 'android':
        driver = get_android(get_data('Udid'))
    elif get_data('PlatformName').lower() == 'ios':
        driver = get_ios(get_data('Udid'))
    else:
        driver = None
        raise Exception('Input is unavailable. The mobile OS is unknown')
    return driver

# This function returns electron driver
def get_electron_driver():
    # options = webdriver.ChromeOptions()
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('ElectronApp')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('ElectronDriver'))
    return driver

# This function returns Chrome webdriver

def get_chrome():
    # chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


# This function returns Firefox webdriver
def get_firefox():
    firefox_driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return firefox_driver


# This function returns Edge webdriver
def get_edge():
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


# This function returns android driver
def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('AppPackage')
    dc['appActivity'] = get_data('AppActivity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('AppiumServer'), dc)
    return android_driver

# This function returns ios driver
def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('BundleId')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('AppiumServer'), dc)
    return ios_driver

# This function returns desktop driver
def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('AppName')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = selenium.webdriver.Remote(get_data('WinAppDriverService'), dc)
    return driver


# This function saves a screenshot as a file in the event of a failure.
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:
            image = get_data('ScreenShotPath') + 'screen_' + str(get_time()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)


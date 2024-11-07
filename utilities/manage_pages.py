
import test_cases.conftest as conf
from page_objects.desktop_objects.calculator_page import ClockCalculatorPage
from page_objects.electron_objects.electron_main_page import ElectronMainPage
from page_objects.mobile_objects.catalog_page import CatalogPage
from page_objects.mobile_objects.electronics_page_m import ELectronicsPageMobile
from page_objects.mobile_objects.home_page import HomePage
from page_objects.mobile_objects.shopping_cart import ShoppingCartM
from page_objects.web_objects_atidstore.checkout_atidstore import CheckoutAtidStore
from page_objects.web_objects_atidstore.item_atidstore import ItemAtidStore
from page_objects.web_objects_atidstore.main_page_atidstore import MainPageAtidStore
from page_objects.web_objects_atidstore.store_atidstore import StoreAtidStore
from page_objects.web_objects_avengers.captain_america_page import CaptainAmerica
from page_objects.web_objects.computers_menu import ComputersMenu
from page_objects.web_objects_avengers.iron_man_page import IronMan
from page_objects.web_objects.log_in_page import LogInPage
from page_objects.web_objects.main_page_upper_menu import MainPageUpperMenu
from page_objects.web_objects.notebooks import Notebooks
from page_objects.web_objects.products_menu_page import ProductsMenuPage
from page_objects.web_objects.register_page import Register
from page_objects.web_objects.search_store import SearchStore
from page_objects.web_objects.shopping_cart import ShoppingCart
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects_avengers.main_page_avengers import MainPageAvengers
from page_objects.web_objects_avengers.the_hulk_page import TheHulkPage
from page_objects.web_objects_avengers.thor_page import ThorPage

# WebObjects
web_register_page = None
web_shopping_cart = None
web_main_page = None
web_main_page_upper_menu = None
web_computers_menu = None
web_products_menu = None
web_search_store = None
web_notebooks = None
web_log_in_page = None
mobile_home_page = None
mobile_shopping_cart = None
mobile_electronics_page = None
mobile_catalog_page = None
electron_main_page_tests = None
clock_calculator_page = None
main_page_avengers = None
iron_man_page = None
captain_america_page = None
the_hulk_page = None
thor_page = None
main_page_atidstore = None
store_atidstore = None
item_atidstore = None
checkout_atidstore = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_register_page'] = Register(conf.driver)
        globals()['web_shopping_cart'] = ShoppingCart(conf.driver)
        globals()['web_main_page'] = MainPage(conf.driver)
        globals()['web_main_page_upper_menu'] = MainPageUpperMenu(conf.driver)
        globals()['web_computers_menu'] = ComputersMenu(conf.driver)
        globals()['web_products_menu'] = ProductsMenuPage(conf.driver)
        globals()['web_search_store'] = SearchStore(conf.driver)
        globals()['web_notebooks'] = Notebooks(conf.driver)
        globals()['web_log_in_page'] = LogInPage(conf.driver)

    @staticmethod
    def init_web_pages_avengers():
        globals()['main_page_avengers'] = MainPageAvengers(conf.driver)
        globals()['iron_man_page'] = IronMan(conf.driver)
        globals()['captain_america_page'] = CaptainAmerica(conf.driver)
        globals()['the_hulk_page'] = TheHulkPage(conf.driver)
        globals()['thor_page'] = ThorPage(conf.driver)

    @staticmethod
    def init_web_pages_atidstore():
        globals()['main_page_atidstore'] = MainPageAtidStore(conf.driver)
        globals()['store_atidstore'] = StoreAtidStore(conf.driver)
        globals()['item_atidstore'] = ItemAtidStore(conf.driver)
        globals()['checkout_atidstore'] = CheckoutAtidStore(conf.driver)


    @staticmethod
    def init_mobile_pages():
        globals()['mobile_home_page'] = HomePage(conf.driver)
        globals()['mobile_shopping_cart'] = ShoppingCartM(conf.driver)
        globals()['mobile_electronics_page'] = ELectronicsPageMobile(conf.driver)
        globals()['mobile_catalog_page'] = CatalogPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_main_page_tests'] = ElectronMainPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['clock_calculator_page'] = ClockCalculatorPage(conf.driver)

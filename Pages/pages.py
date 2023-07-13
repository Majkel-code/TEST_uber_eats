from Pages.uber_search_page import UberSearchPage
from Pages.restaurant_list import RestaurantsList
from Pages.load_new_page import LoadPage


class Pages:
    def __init__(self, driver):
        self.uber_search_page = UberSearchPage(driver)
        self.restaurants_list = RestaurantsList(driver)
        self.load_page = LoadPage(driver)

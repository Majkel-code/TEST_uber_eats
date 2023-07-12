import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from base_page import BasePage
from pages import Pages
from uber_search_page import UberSearchPage


def read_test_data():
	test_data = {}
	with open("test_data.json", "r") as f:
		test_data = json.load(f)
	return test_data


def get_driver():
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	return driver


def setup():
	base_url = "https://www.ubereats.com/pl"
	driver = get_driver()
	driver.get(base_url)
	pages = Pages(driver)
	return {
		'pages': pages,
		'driver': driver
	}


@pytest.mark.parametrize('data', [read_test_data()])
def test_data(data):
	assert data["search_address"] == "Krakow Tischnera Office"
	assert data["expected_restaurant"] == "McDonald"
	assert data["data_test_id"] == "store-card"
	assert data["button_class"] == "i8"

# ----------------------
# coś tu nie gra, odpala się dwa razy Chrome, skrypt używa tylko pierwszego, drugi stoi w idle
setup_data = setup()
pages = setup_data['pages']
base_page = BasePage(setup_data['driver'])
# -----------------------------------


@pytest.mark.parametrize('data', [read_test_data()])
def test_uber_start_page(data):
	#------- wyjaśnienie wyżej --------
	# setup_data = setup()
	# pages = setup_data['pages']
	# ----------------------------------------
	assert pages.uber_search_page.location_box.text == ''
	pages.uber_search_page.location_box.send_keys(data["search_address"])
	assert pages.uber_search_page.location_box.get_attribute("value") == f'{data["search_address"]}'
	assert pages.uber_search_page.search_results_list == {'result': True, 'error': None}
	pages.uber_search_page.search_results_list_first_element.click()
	assert pages.uber_search_page.new_page_button == {'result': True, 'error': None}
	assert data["button_class"] in pages.uber_search_page.button.get_attribute("class")


@pytest.mark.parametrize('data', [read_test_data()])
def test_search_restaurant(data):
	assert base_page.wait(class_name=data['button_class']) == {'result': True, 'error': None}
	assert pages.restaurants_list.get_restaurant_container_list(data['data_test_id']) == {'result': True, 'error': None}
	assert pages.restaurants_list.find_expected_restaurant(data['expected_restaurant']) == {'result': True, 'error': None}
	assert pages.restaurants_list.click_restaurant == {'result': True, 'error': None}

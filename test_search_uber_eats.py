
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def read_test_data():
	"""
	Read "test_data.json" file and parse it nto dictionary
	:return: test_data : dict
	"""
	with open("test_data.json", "r") as f:
		test_data = json.load(f)
	return test_data


def find_restaurant_container_dom(driver, data_test_id_value):
	"""
	Look for every element on th page with specific "data_testid" from file test_data.json

	-----
	:param driver: WebDriver object
	:param data_test_id_value: specific value what will be looking on Website
	:return: list of every object that contains "data_test_id_value"
	"""
	restaurants_container_list = []
	for restaurant in driver.find_elements(By.XPATH, f"//div[@data-testid='{data_test_id_value}']"):
		restaurants_container_list.append(restaurant)
	return restaurants_container_list


def find_location(driver, location, wait):
	"""
	The find_location function takes in a driver and location as parameters.
	It then finds the location box on the page, enters the given location into it,
	and clicks on the first option that appears. It returns True if successful.

	-----
	:param driver: Access the webdriver object
	:param location: Specify the location that you want to search for
	:param wait: Wait for the page to load before continuing
	:return: True if the location is found, and false otherwise
	:doc-author: Trelent
	"""
	try:
		location_box = driver.find_element(By.ID, value="location-typeahead-home-input")
		location_box.send_keys(location)
		wait.until(EC.element_to_be_clickable((By.ID, "location-typeahead-home-item-0")))
		driver.find_element(By.ID, "location-typeahead-home-item-0").click()
		wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "i8")))
		return True
	except:
		return False


def load_new_page(driver):
	"""
	Find button who loads new page on website

	-----
	:param driver: Webdriver object
	:return: True/False depends on successful loads new page
	"""
	sleep(2)
	try:
		driver.find_element(By.CLASS_NAME, "i8").click()
		return True
	except:
		return False


def find_restaurant(choice, restaurants_container_list):
	"""
	Looking for choices restaurant near given location

	-----
	:param choice: name of looked restaurant
	:param restaurants_container_list: a list which contains specific data_testid objects
	:return: True if successful find restaurant
	"""
	for restaurant in restaurants_container_list:
		check_restaurant = restaurant.find_element(By.CSS_SELECTOR, "div.ak.bl > a")
		if check_restaurant.get_attribute("href") and choice in check_restaurant.text:
			restaurant.click()
			return True
		else:
			continue


def script_service():
	"""
	The script_service function is the main function of this script.
	It takes no arguments and returns True if the expected restaurant was found, False otherwise.
	The function uses a webdriver to open a browser window and navigate to https://ubereats.com/pl/.
	Then it searches for an address provided in test_data file (search_address key) using find_location function,
	and then finds all restaurants on that page using find_restaurant_container dom method with data-test-id value from test_data file (data-test-id key).
	After that it checks if any of those restaurants

	-----
	:return: True if the restaurant is found
	:doc-author: Trelent
	"""
	test_data = read_test_data()
	base_url = "https://www.ubereats.com/pl"
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	wait = WebDriverWait(driver, timeout=30)
	driver.get(base_url)
	print(driver.title)
	if test_data["search_address"] and test_data["expected_restaurant"] and base_url == driver.current_url:
		page_found = find_location(driver=driver, location=test_data["search_address"], wait=wait)
		restaurants_container_list = find_restaurant_container_dom(driver=driver, data_test_id_value=test_data["data_test_id"])
		while page_found:
			if find_restaurant(choice=test_data["expected_restaurant"], restaurants_container_list=restaurants_container_list):
				return True
			else:
				if load_new_page(driver):
					continue
				else:
					return False


def test_uber_eats_search():
	assert script_service() is True

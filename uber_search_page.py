from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage


class UberSearchPage(BasePage):

	@property
	def location_box(self):
		return self._driver.find_element(By.ID, value="location-typeahead-home-input")

	@property
	def search_results_list_first_element(self):
		return self._driver.find_element(By.ID, value="location-typeahead-home-item-0")

	@property
	def search_results_list(self):
		try:
			if self._wait.until(EC.element_to_be_clickable((By.ID, "location-typeahead-home-item-0"))):
				return {'result': True, 'error': None}
		except Exception as e:
			return {'result': False, 'error': e}

	@property
	def new_page_button(self):
		try:
			if self._wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "i8"))):
				return {'result': True, 'error': None}
		except Exception as e:
			return {'result': False, 'error': e}

	@property
	def button(self):
		return self._driver.find_element(By.CLASS_NAME, "i8")

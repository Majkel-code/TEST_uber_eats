from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from Config.decorators import return_result_and_error


class UberSearchPage(BasePage):

	@property
	def location_box(self):
		return self._driver.find_element(By.ID, value="location-typeahead-home-input")

	@property
	def search_results_list_first_element(self):
		return self._driver.find_element(By.ID, value="location-typeahead-home-item-0")

	@property
	@return_result_and_error
	def search_results_list(self):
		self._wait.until(EC.element_to_be_clickable((By.ID, "location-typeahead-home-item-0")))
		return True

	@property
	@return_result_and_error
	def new_page_button(self):
		return self.find_button_by_text("Pokaż więcej")

	def button(self, class_name):
		return self._driver.find_element(By.CLASS_NAME, class_name)

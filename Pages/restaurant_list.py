from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Config.decorators import return_result_and_error
from time import sleep


class RestaurantsList(BasePage):

	@return_result_and_error
	def get_restaurant_container_list(self, data_test_id):
		sleep(2)
		self._restaurants_list = self._driver.find_elements(By.XPATH, f"//div[@data-testid='{data_test_id}']")
		return True

	@return_result_and_error
	def find_expected_restaurant(self, expected_restaurant, data_test_id):
		iteration = 0
		while self._restaurants_list:
			if iteration >= len(self._restaurants_list) and self.load_new_page():
				self.get_restaurant_container_list(data_test_id)
				iteration = 0
			print(len(self._restaurants_list))
			print(iteration)
			restaurant = self._restaurants_list[iteration]
			restaurant_link = self.find_restaurant_link(restaurant)
			print(restaurant_link.text)
			if expected_restaurant in restaurant_link.text:
				self._restaurant = restaurant
				return True
			else:
				iteration += 1
				continue

	def load_new_page(self):
		sleep(2)
		self._driver.find_element(By.CLASS_NAME, "i8").click()
		return True

	def find_restaurant_link(self, restaurant):
		return restaurant.find_element(By.CSS_SELECTOR, "div.ak.bl > a")

	@property
	@return_result_and_error
	def click_restaurant(self):
		self._restaurant.click()
		return True

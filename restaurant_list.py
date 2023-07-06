from selenium.webdriver.common.by import By
from load_new_page import LoadPage
from base_page import BasePage


class RestaurantsList(BasePage):

	def get_restaurant_container_list(self, data_test_id):
		try:
			self._restaurants_list = self._driver.find_elements(By.XPATH, f"//div[@data-testid='{data_test_id}']")
			return {'result': True, 'error': None}
		except Exception as e:
			return {'result': False, 'error': e}

	def find_expected_restaurant(self, expected_restaurant):
		for restaurant in self._restaurants_list:
			restaurant_link = self.find_restaurant_link(restaurant)
			if expected_restaurant in restaurant_link.text:
				self._restaurant = restaurant
				return {'result': True, 'error': None}
			else:
				try:
					load_page = LoadPage.load_new_page(self._driver)
					if load_page["result"]:
						continue
					else:
						return {'result': False, 'error': load_page['error']}
				except Exception as e:
					return {'result': False, 'error': e}

	def find_restaurant_link(self, restaurant):
		try:
			return restaurant.find_element(By.CSS_SELECTOR, "div.ak.bl > a")
		except Exception as e:
			return {'result': False, 'error': e}

	@property
	def click_restaurant(self):
		try:
			self._restaurant.click()
			return {'result': True, 'error': None}
		except Exception as e:
			return {'result': False, 'error': e}

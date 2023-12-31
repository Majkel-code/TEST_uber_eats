from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BasePage:
	def __init__(self, driver):
		self._wait = WebDriverWait(driver, timeout=30)
		self._driver = driver
		self._restaurant = ''
		self._restaurants_list = []

	def wait(self, class_name):
		seconds = 0
		try:
			while seconds <= 30:
				element = self._driver.find_element(By.CLASS_NAME, class_name)
				sleep(1)
				seconds += 1
				if element:
					break
			return {'result': True, 'error': None}
		except:
			return {'result': False, 'error': TimeoutError}

	def search_by_data_test_id(self, data_test_id_value):
		return self._driver.find_element(By.XPATH, value=f"//[@data-testid='{data_test_id_value}']")

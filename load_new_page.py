from time import sleep
from base_page import BasePage
from selenium.webdriver.common.by import By


class LoadPage(BasePage):

	def load_new_page(self):
		sleep(2)
		try:
			self._driver.find_element(By.CLASS_NAME, "i8").click()
			return {'result': True, 'error': None}
		except Exception as e:
			return {'result': False, 'error': e}

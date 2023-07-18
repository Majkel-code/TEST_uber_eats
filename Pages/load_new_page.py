from time import sleep
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoadPage(BasePage):

	def load_new_page(self):
		sleep(2)
		self._driver.find_element(By.CLASS_NAME, "i8").click()
		return True

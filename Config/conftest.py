from pytest import fixture
from selenium import webdriver
from Pages.base_page import BasePage
from Pages.pages import Pages



@fixture(autouse=True)
def prepare_something():
	print("Prepare something before test")
	yield
	print("Cleanup after test")


@fixture(autouse=True, scope='session')
def cleanup(driver):
	yield driver
	driver.close()


@fixture(scope='session')
def driver():
	base_url = "https://www.ubereats.com/pl"
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	driver.get(base_url)
	return driver


@fixture(scope='session')
def pages(driver):
	print("Get driver")
	page_objects = Pages(driver)
	base_page = BasePage(driver)
	return {
		"pages": page_objects,
		"base_page": base_page
	}

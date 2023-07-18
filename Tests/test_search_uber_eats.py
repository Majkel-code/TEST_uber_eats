import pytest
from Config.read_json_data import read_test_data


@pytest.mark.parametrize('data', [read_test_data()])
def test_data(data):
	assert data["search_address"] == "Krakow Tischnera Office"
	assert data["expected_restaurant"] == "McDonald"


@pytest.mark.parametrize('data', [read_test_data()])
def test_uber_start_page(data, pages):
	assert pages.uber_search_page.location_box.text == ''
	pages.uber_search_page.location_box.send_keys(data["search_address"])
	assert pages.uber_search_page.search_results_list == {'result': True, 'error': []}
	pages.uber_search_page.search_results_list_first_element.click()
	pages.uber_search_page.new_page_button
	pages.restaurants_list.show_more_button
	found_restaurant = pages.restaurants_list.find_restaurant_in_list_of_restaurants(data['expected_restaurant'])
	found_restaurant.click()

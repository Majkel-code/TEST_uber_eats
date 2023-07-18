import pytest
from Config.read_json_data import read_test_data


@pytest.mark.parametrize('data', [read_test_data()])
def test_data(data):
	assert data["search_address"] == "Krakow Tischnera Office"
	assert data["expected_restaurant"] == "McDonald"
	assert data["data_test_id"] == "store-card"
	assert data["button_class"] == "i8"


@pytest.mark.parametrize('data', [read_test_data()])
def test_uber_start_page(data, pages):
	assert pages["pages"].uber_search_page.location_box.text == ''
	pages["pages"].uber_search_page.location_box.send_keys(data["search_address"])
	assert pages["pages"].uber_search_page.search_results_list == {'result': True, 'error': []}
	pages["pages"].uber_search_page.search_results_list_first_element.click()
	assert pages["pages"].uber_search_page.new_page_button(class_name=data['button_class']) == {'result': True, 'error': []}


@pytest.mark.parametrize('data', [read_test_data()])
def test_search_restaurant(data, pages):
	assert pages["base_page"].wait(class_name=data['button_class']) == {'result': True, 'error': []}
	assert pages["pages"].restaurants_list.get_restaurant_container_list(data['data_test_id']) == {'result': True, 'error': []}
	assert pages["pages"].restaurants_list.find_expected_restaurant(data['expected_restaurant'], data['data_test_id']) == {'result': True, 'error': []}
	assert pages["pages"].restaurants_list.click_restaurant == {'result': True, 'error': []}

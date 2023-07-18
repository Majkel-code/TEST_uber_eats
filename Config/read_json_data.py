import json


def read_test_data():
	test_data = {}
	with open("test_data.json", "r") as f:
		test_data = json.load(f)
	return test_data

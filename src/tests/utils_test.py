from src.db.database import Database

__author__ = 'jslvtr'

import unittest
from src.app import Utils


class UtilsTest(unittest.TestCase):

    def test_create_response_data(self):
        data = Utils.create_response_data("Test", 500)
        self.assertEqual(data['data'],
                         "Test",
                         "Data created via `create_response_data` is not equal to input data!")
        self.assertEqual(data['status_code'],
                         500,
                         "Status code created via `create_response_data` is not equal to input status code!")

    def test_create_response_error(self):
        data = Utils.create_response_error("InternalServerError", "The Server could not fulfil your request", 500)
        self.assertEqual(data['error']['name'],
                         "InternalServerError",
                         "Error name created via `create_response_error` is not equal to input!")
        self.assertEqual(data['error']['message'],
                         "The Server could not fulfil your request",
                         "Error message created via `create_response_error` is not equal to input!")
        self.assertEqual(data['status_code'],
                         500,
                         "Status code created via `create_response_error` is not equal to input status code!")

    def test_check_authorization(self):



if __name__ == '__main__':
    unittest.main()

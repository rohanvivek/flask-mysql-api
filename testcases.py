"""Unit test cases for the flask app."""

import unittest
import json
from app import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        """Testing response by putting after '/'"""
        response = self.app.get('/')
        # loading data in response
        response = json.loads(response.data.decode())
        self.assertEqual("Hello World!", response['data'])

    def test_customer_id(self):
        """Test if invalid id is passed"""
        response = self.app.get(
            '/customers/VYTFR')
        response = json.loads(response.data.decode())
        self.assertEqual('No Customer Found', response['data'])

    def test_product_id(self):
        """Test when invalid product_id is passed"""
        response = self.app.get(
            '/products/675')
        response = json.loads(response.data.decode())
        self.assertEqual('No Product Found', response['data'])

    def test_order_id(self):
        """Test if data is not available for given id"""
        response = self.app.get('/orderhistory/WEARE')
        response = json.loads(response.data.decode())
        self.assertEqual('No Orders Found', response['data'])

    def test_unknown_endpoint(self):
        """Test if end point is unknown"""
        response = self.app.get('/products/xyz/abc')
        response = response.status.split()
        self.assertEqual('404', response[0])

    def test_valid_contact_name(self):
        """Test for validating data"""
        response = self.app.get('/products/18')
        response = json.loads(response.data.decode())
        self.assertEqual("Carnarvon Tigers", response['ProductName'])

    def test_country_name_mixedcase(self):
        """Handeling mixed character"""
        response = self.app.get('/customers/aLfkI')
        response = json.loads(response.data.decode())
        self.assertEqual("Maria Anders", response['ContactName'])


if __name__ == '__main__':
    unittest.main()

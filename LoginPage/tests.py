# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import vehicle_choice

class LoginTestCase(TestCase):

    def test_get_login_feature(self):
    	"""Unit Test for Get feature in LoginPage View"""
        response = self.client.get('/LoginPage/')
        self.assertAlmostEqual(response.status_code, 200)

    def test_post_login_feature(self):
    	"""Unit Test for POST feature in LoginPage View"""
        response = self.client.post('/LoginPage/', {'vehivles': ['Nikola 2.0'], 'csrfmiddlewaretoken': ['KNFLaTSErT5x24bymyI1ToVNTnuXafpVHvEiSbqTLNVzvzQfnvI8TGL4kKqPAdxB'], 'password': ['Qwerty123$'], 'user_id': ['sandeep']})
        self.assertAlmostEqual(response.status_code, 200)

    def test_vehicles(self):
    	"""Unit Test for testing vehivle_choice returns a data or not"""
    	response = vehicle_choice()
    	self.assertAlmostEqual(len(response) > 0, True)

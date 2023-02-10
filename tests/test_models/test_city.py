#!/usr/bin/python3
"""testing City"""

import unittest
import pep8
from models.city import City

class City_testing(object):
	""" Checks the base model """
	
	def testpep8(self):
		"""testing the style of code"""
		pepstylecode = pep8.StyleGuide(quiet = True)
		path_city = 'models/city.py'
		result = pepstylecode.check_files([path_city])
		self.assertEqual(result.total_errors, 0,
						 "Found Codestyle Errors and Warnings")
#!/usr/bin/python3
"""testing Place"""

import unittest
import pep8
from models.place import Place

class Place_testing(object):
	""" Checks the base model """
	
	def testpep8(self):
		"""testing the style of code"""
		pepstylecode = pep8.StyleGuide(quiet = True)
		path_place = 'models/place.py'
		result = pepstylecode.check_files([path_place])
		self.assertEqual(result.total_errors, 0,
						 "Found Codestyle Errors and Warnings")
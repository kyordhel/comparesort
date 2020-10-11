#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# bubblesort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def bubblesort(array):
	"""Sorts the provided Array object using the Bubblesort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Bubblesort Algorithm
	pass
#end def

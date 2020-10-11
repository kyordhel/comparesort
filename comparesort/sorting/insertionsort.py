#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ## ###############################################################
# insertionsort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def insertionsort(array):
	"""Sorts the provided Array object using the Insertion Sort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Insertion Sort Algorithm
	for i in range(1, len(array)):
		greatest = array[i]

		# Move forward those elements in the subarray A[0...i-1]
		# which are greater than 'greatest'
		j = i-1
		while j >= 0 and greatest < array[j]:
			array[j+1] = array[j]
			j-= 1
		# Insert greatest in place
		array[j+1] = greatest
	#end for
#end def

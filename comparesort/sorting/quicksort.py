#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# quicksort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def quicksort(array):
	"""Sorts the provided Array object using the Quicksort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Quicksort Algorithm
	recursive_quicksort(array, 0, len(array))
#end def

def recursive_quicksort(a, p, r):
	"""Sorts the provided Array object using the Quicksort algorithm"""
	# Quicksort Algorithm
	if p < r:
		q = partition(a, p, r)
		recursive_quicksort(a, p, q-1)
		recursive_quicksort(a, q+1, r)
#end def

def partition(a, p, r):
	pass
#end def

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# selectionsort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def selectionsort(array):
	"""Sorts the provided Array object using the Selection Sort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Selection Sort Algorithm
	for i in range(len(array)):
		# Find smallest unsorted element in Array:
		ix_min = i
		for j in range(i+1, len(array)):
			if array[ix_min] > array[j]:
				ix_min = j
		# Swap the smallest element found with the firs element of the
		# unsorted sub-array
		array.swap(i, ix_min)
	#end for
#end def

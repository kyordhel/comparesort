#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ## ###############################################################
# heapsort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def heapsort(array):
	"""Sorts the provided Array object using the Heapsort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Heapsort Algorithm
	pass
#end def

def build_max_heap(a, i):
	pass
#end def

def max_heapify(a, i):
	pass
#end def

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# mergesort.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

from comparesort.array import Array

def mergesort(array):
	"""Sorts the provided Array object using the Mergeksort algorithm"""
	if isinstance(array, list):
		array = Array(array) # Converts the list to an Array
	if not isinstance(array, Array):
		raise TypeError("Expected a list or Array object")

	# Mergesort Algorithm
	pass
#end def

def recursive_mergesort(a, p, r):
	if p < r:
		q = int( (p+r) / 2)
		recursive_mergesort(a, p, q)
		recursive_mergesort(a, q+1, r)
		merge(a, p, q, r)
#end def

def merge(a, p, q, r):
	pass
#end def

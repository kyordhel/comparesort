#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# array.py
#
# Author: Mauricio Matamoros
#
# ## ###############################################################

class Array(object):
	"""An array that counts how many times it has been accessed"""

	def __init__(self, array=[]):
		"""Initializes the array

		Keyword arguments:
		array -- a list containing the object to initialize the Array with
		"""
		if not isinstance(array, list):
			array = [array]
		self.__array = list(array)
		self.__accesses = 0
	#end def

	def __len__(self):
		"""Gets the count of objects stored in the Array"""
		return len(self.__array)
	#end def

	def __getitem__(self, index):
		"""Gets the object at position index"""
		self.__accesses+= 1
		return self.__array[index]
	#end def

	def __setitem__(self, index, value):
		"""Sets the object at position index"""
		self.__accesses+= 1
		self.__array[index] = value
	#end def

	@property
	def accesses(self):
		"""Returns the number of times Array has been read or written"""
		return self.__accesses
	#end def

	def reset(self):
		"""Resets the accesses counter to zero"""
		self.__accesses = 0
	#end def

	def swap(self, ix, jx):
		"""Exchanges the objects at position ix and jx"""
		self[ix], self[jx] = self[jx], self[ix]
	#end def
#end class

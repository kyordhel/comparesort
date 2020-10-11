#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# generator.py
#
# Sequence generador for bucket sort
#
# Author: Mauricio Matamoros
#
# ## ###############################################################

import random
from comparesort.array import Array

minimum = -1000
maximum = 1000
random.seed(a=69)

def get_array(count):
	"""Returns an Array object with count random values"""
	return Array([ random.uniform(minimum, maximum) for i in range(count) ])

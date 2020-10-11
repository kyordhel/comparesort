#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# __main__.py
#
# Author: Mauricio Matamoros
#
# ## ###############################################################

import os
import csv
import time
from . import generator
from .data import datafile

def _prettify_name(str):
	"""Prettifies the name of the sorting algorithm function"""
	return str[0].upper() + str[1:].replace("sort", " Sort")
#end def

def _prepare_data_file(file):
	writer = csv.writer(file, dialect="excel")
	writer.writerow(["Sorting Method", "Array Size", "Accesses", "Sorting Time"])
	return writer

def benchmark(sorting_functions, max_array_size, initial_array_size=100, step=10):
	"""Benchmarks a set of sorting functions over arrays
	of differnt sizes and stores the results in a datafile"""
	array_size = initial_array_size

	with open(datafile, "w", newline="") as f:
		writer = _prepare_data_file(f)
		while array_size <= max_array_size:
			A = generator.get_array(array_size)
			for sf in sorting_functions:
				accesses, run_time = benchmark_f(sf, A)
				writer.writerow([
					sf.__name__,
					array_size,
					accesses,
					"{:.1f}".format(run_time)
				])
			if array_size < max_array_size:
				array_size = min(max_array_size, int(array_size * step))
			else:
				array_size = int(array_size * step)
	#end with and close file
#end def


def benchmark_f(sorting_function, array):
	"""Benchmarks a sorting function over an array"""
	start_time = time.time()
	for i in range(10):
		array.reset()
		sorting_function(array)
	run_time = (time.time() - start_time) * 100000
	print_summary(sorting_function.__name__, array, run_time)
	return array.accesses, run_time
#end def


def print_summary(sorting_name, array, run_time):
	"""Prints the summary of the sorting operation"""
	print("{} with {} elements:".format(_prettify_name(sorting_name), len(array)))
	print("  Accesses to Array: {}".format(array.accesses))
	print("  Sorting time:      {0:.1f}us".format(run_time))
#end def

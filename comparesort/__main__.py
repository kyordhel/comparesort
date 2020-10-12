#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# __main__.py
#
# Author: Mauricio Matamoros
#
# ## ###############################################################

from comparesort.benchmark import plot_time
from comparesort.benchmark import plot_access
from comparesort.benchmark import benchmark
from comparesort.sorting import insertionsort
from comparesort.sorting import selectionsort
from comparesort.sorting import bubblesort
from comparesort.sorting import quicksort
from comparesort.sorting import mergesort
from comparesort.sorting import heapsort

max_array_size = 100000

def main():
	"""Main entry point"""
	algorithms = [
		# selectionsort,
		insertionsort,
	# Uncommend these lines after implementing algorithms
		# bubblesort,
		# quicksort,
		# mergesort,
		# heapsort,
	]

	benchmark(algorithms, max_array_size, initial_array_size=100, step=5)
	plot_time()
	# plot_access()
#end def

if __name__ == '__main__':
	main()

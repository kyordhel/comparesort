#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# __main__.py
#
# Author: Mauricio Matamoros
#
# ## ###############################################################

from comparesort.benchmark import plot
from comparesort.benchmark import benchmark
from comparesort.sorting import insertionsort
from comparesort.sorting import selectionsort
from comparesort.sorting import bubblesort
from comparesort.sorting import quicksort
from comparesort.sorting import mergesort
from comparesort.sorting import heapsort

max_array_size = 1000000

def main():
	"""Main entry point"""
	algorithms = [
		selectionsort,
		insertionsort,
	# Uncommend these lines after implementing algorithms
		# bubblesort,
		# quicksort,
		# mergesort,
		# heapsort,
	]

	benchmark(algorithms, max_array_size)
	plot()
#end def

if __name__ == '__main__':
	main()

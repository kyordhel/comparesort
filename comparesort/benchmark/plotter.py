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
import matplotlib.pyplot as plt

from .data import datafile

def _new_dataset():
	"""Returns a new data row"""
	return { "x" : [], "y" : [], "t" : [] }

def _add2dataset(dataset, row):
	dataset["x"].append(int(row["Array Size"]))
	dataset["y"].append(int(row["Accesses"]))
	dataset["t"].append(float(row["Sorting Time"]))
# end def


def _read_data():
	"""Reads the data from the datafile"""
	data = {}
	with open(datafile, "r", newline="") as f:
		reader = csv.DictReader(f)
		for row in reader:
			if not row["Sorting Method"] in data:
				data[row["Sorting Method"]] = _new_dataset()
			_add2dataset(data[row["Sorting Method"]], row)
	#end with and close file
	return data
# end def





def _plot_series(axis, xdata, ydata, color, label):
	"""Plots one series"""
	axis.plot(xdata, ydata, "{}-".format(color[0]), label=label)
	axis.plot(xdata, ydata, "{}".format(color))
# end def

def plot_access():
	"""Plots the data of the datafile"""
	data = _read_data()
	colors = ["ro", "go", "bo", "ys", "cX", "mX", "kx"]

	f, ax = plt.subplots(1)

	i = 0
	for sortingmethod in data:
		_plot_series(
			ax,
			data[sortingmethod]["x"],
			data[sortingmethod]["y"],
			colors[i%len(colors)],
			sortingmethod[0].upper() + sortingmethod[1:].replace("sort", " Sort")
		)
		i+=1
	# end for
	ax.grid()
	plt.xlabel("Array size")
	plt.ylabel("Array IO operations (read/write)")
	plt.legend()
	plt.show()
# end def

def plot_time():
	"""Plots the data of the datafile"""
	data = _read_data()
	colors = ["ro", "go", "bo", "ys", "cX", "mX", "kx"]

	f, ax = plt.subplots(1)

	i = 0
	for sortingmethod in data:
		_plot_series(
			ax,
			data[sortingmethod]["x"],
			data[sortingmethod]["t"],
			colors[i%len(colors)],
			sortingmethod[0].upper() + sortingmethod[1:].replace("sort", " Sort")
		)
		i+=1
	# end for
	ax.grid()
	plt.xlabel("Array size")
	plt.ylabel("Sorting time")
	plt.legend()
	plt.show()
# end def


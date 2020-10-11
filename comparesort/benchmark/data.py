#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# data.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# ## ###############################################################

import os
import comparesort

datapath = os.path.dirname(os.path.abspath(comparesort.__file__))
datapath = os.path.join(datapath, "data")
if not os.path.exists(datapath):
	os.mkdir(datapath)
datafile = os.path.join(datapath, "benchmark_results.csv")

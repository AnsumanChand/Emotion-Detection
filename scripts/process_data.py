# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:58:28 2020

@author: ansuman
"""
import os
import sys
import argparse

import yaml
import numpy as np
import pandas as pd

from dataprep import ReadFile

parser = argparse.ArgumentParser(description="Emotion Detect - Data Process ")
parser.add_argument('params_file', metavar='FILENAME', type=str, help='Parameter file name in yaml format')
args = parser.parse_args()

try:
    params = yaml.load(open(args.params_file))
except:
    print('Error loading parameter file: {args.params_file}.')
    sys.exit(1)
print("Printing Parameters {}".format(params))

rfile = ReadFile(params['data_path'])
data = rfile.getdata()
print(data.head())

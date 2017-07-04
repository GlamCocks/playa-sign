#!/usr/bin/env python

import json
import os 
import yaml
import itertools

filename = 'layout.json'

def writePixel(x, y):
	pixels.append({'point': [x, 0, y]})

pixels = []
channels_size = [{'width': 0, 'height': 0}] * 6 * 8

if os.path.isfile(filename):
	os.remove(filename)

with open('config.yml', 'r') as f:
    config = yaml.load(f)

for pixel in config['pixels']:
	x = pixel['x']
	y = pixel['y'] 

	if x == 0 and y == 0: 
		writePixel(1000, 1000)
	else:
		writePixel(x * 8.9252 - 8.9252/2 , y * 3.27 - 3.27/2)

with open(filename, 'w') as outfile:
    json.dump(pixels, outfile)
#!/usr/bin/env python

import json
import os 
import yaml
import itertools

filename = 'layout.json'

def writePixel(x, y):
	pixels.append({'point': [x, 0, y]})

pixels = []

last_channel = 0
last_index = 0

with open('config.yml', 'r') as f:
    config = yaml.load(f)

for pixel in config['pixels']:
	channel = pixel[0]
	index = pixel[1] 
	x = pixel[2] * 3 - 2
	y = pixel[3] * 6 - 4

	if channel - last_channel > 1:
		for _ in itertools.repeat(None, (channel - last_channel) * 64):
			writePixel(1000, 1000)
	elif channel - last_channel == 1:
		for _ in itertools.repeat(None, 63 - last_index):
			writePixel(1000, 1000)

	writePixel(x, y)

	last_channel = channel
	last_index = index

with open(filename, 'w') as outfile:
    json.dump(pixels, outfile)


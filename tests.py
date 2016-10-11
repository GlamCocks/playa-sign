#!/usr/bin/env python

import time 

from lib import *

server = Server(config_file="config.yml")
server.colorspace_correction = False

letter = server.letters[1]

for channel in letter.channels:
	print "Loading " + str(channel) + "..."

	for pixel in channel.pixels:
		pixel.color = [0, 0, 0]
		server.push()
		pixel.color = [255, 0, 0]
		server.push()
		time.sleep(0.05)

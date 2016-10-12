#!/usr/bin/env python

import time 

from lib import *

server = Server(config_file="config.yml")
server.colorspace_correction = False

server.clean()
server.push()

for loop in Loop.instances:
	print str(loop)
# for letter in server.letters:
# 	for loop in letter.loops:
# 		first_node = loop.nodes[0]
# 		print str(first_node)
# letter = server.letters[1]

# for channel in letter.channels:
# 	print "Loading " + str(channel) + "..."

# 	for pixel in channel.pixels:
# 		pixel.color = [0, 0, 0]
# 		server.push()
# 		pixel.color = [255, 0, 0]
# 		server.push()
# 		time.sleep(0.05)

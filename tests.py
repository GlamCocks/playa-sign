#!/usr/bin/env python

import time 

from lib import *

Server(config_file="config.yml")
Server().colorspace_correction = False

Server().clean()
Server().push()

loop = Loop.instances[0]
chasing_loop = ChasingLoop(loop=loop, fps=200)
chasing_loop.start()

# print str(Color['red'].value(colorspace='GRB'))
# for loop in Loop.instances:
# 	loop.lol(1)
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

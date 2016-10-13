#!/usr/bin/env python

import time 

from lib import *

Server(config_file="config.yml")
Server().colorspace_correction = False

Server().clean()
Server().push()

loop = Loop.instances[0]
chasing_loop_clockwise = ChasingLoop(loop=loop, color=Color['red'], rotation=Rotation.Clockwise)
chasing_loop_clockwise2 = ChasingLoop(loop=loop, color=Color['green'], rotation=Rotation.Clockwise, delay=30)
chasing_loop_counterclockwise = ChasingLoop(loop=loop, color=Color['cyan'], rotation=Rotation.CounterClockwise)
chasing_loop_counterclockwise2 = ChasingLoop(loop=loop, color=Color['yellow'], rotation=Rotation.CounterClockwise, delay=15)

while True:
	chasing_loop_clockwise.render()
	chasing_loop_clockwise2.render()
	chasing_loop_counterclockwise.render()
	chasing_loop_counterclockwise2.render()
	Server().push()
	time.sleep(1.0/30.0)

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

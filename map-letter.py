#!/usr/bin/env python

from lib import *

server = Server(config_file="config.yml")

input_var = input("Which letter # do you want to work on? ")
letter = server.letters[input_var]

print "Working on letter " + str(letter) 

pixels = []

for channel in letter.channels:
	print "Loading channel " + str(channel) + "..."

	if channel.type == "strip":
		print "Channel type is strip, let's load the next one."
		continue

	for pixel in channel.pixels:
		pixel.color = [0, 0, 100]
		server.push()

		input_x = input("What is the X coordinate of this red pixel? ")
		input_y = input("What is the Y coordinate of this red pixel? ")

		pixels.append([channel.index, pixel.index, input_x, input_y])
		print "Mapping... results:"
		print str(pixels)
		pixel.color = [0, 0, 0]
		server.push()

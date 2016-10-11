#!/usr/bin/env python

from lib import *

server = Server(config_file="config.yml")

letter = server.letters[1]

for channel in letter.channels:
	print "Loading " + str(channel) + "..."

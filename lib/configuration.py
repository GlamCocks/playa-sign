#!/usr/bin/env python

import socket
import OSC
import re
import time
import threading
import math
import logging
import types
from animations import *
from structure import *

logger = logging.getLogger("playasign.configuration")

from structure import Singleton

class Configuration(object):
	__metaclass__ = Singleton

	_hasChanged = True 
	animationHasChanged = True

	brightness = 0.5 # [0...1]
	speed = 0.5 # [0...1]
	animation = AnimationType.RainbowWave

	rainbow_wave_scale = 0.7 # [0...1]
	strobe_color = Color['white']
	moving_star_position = [0.0, 0.0] # [x: [0...1], y: [0...1]]

	def __init__(self, server, client):
		self.server = OSC.OSCServer(server)
		self.client = OSC.OSCClient()
		self.client.connect(client)
		self.thread = threading.Thread(target=self.server.serve_forever)
		self.addHandlers()

	def __exit__(self, exc_type, exc_value, traceback):
		self.stop()

	def start(self):
		self.thread.start()

	def stop(self):
		self.server.close()

	def addHandlers(self):
		self.server.addMsgHandler("/general/brightness", self.brightness_handler)
		self.server.addMsgHandler("/general/speed", self.speed_handler)
		self.server.addMsgHandler("/animation/blinking-stars", self.animation_handler)
		self.server.addMsgHandler("/animation/rainbow", self.animation_handler)
		self.server.addMsgHandler("/animation/rainbow-mosaic", self.animation_handler)
		self.server.addMsgHandler("/animation/rainbow-wave", self.animation_handler)
		self.server.addMsgHandler("/animation/rainbow-wave/scale", self.rainbow_wave_scale_handler)
		self.server.addMsgHandler("/animation/strobe/white", self.strobe_white_handler)
		self.server.addMsgHandler("/animation/strobe/yellow", self.strobe_yellow_handler)
		self.server.addMsgHandler("/animation/strobe/orange", self.strobe_orange_handler)
		self.server.addMsgHandler("/animation/strobe/brown", self.strobe_brown_handler)
		self.server.addMsgHandler("/animation/strobe/red", self.strobe_red_handler)
		self.server.addMsgHandler("/animation/strobe/pink", self.strobe_pink_handler)
		self.server.addMsgHandler("/animation/strobe/purple", self.strobe_purple_handler)
		self.server.addMsgHandler("/animation/strobe/blue", self.strobe_blue_handler)
		self.server.addMsgHandler("/animation/moving-star", self.animation_handler)
		self.server.addMsgHandler("/animation/moving-star/position", self.moving_star_position_handler)

	def refreshClient(self):
		if Configuration._hasChanged == False:
			return 

		self.send("/general/brightness", Configuration.brightness)
		self.send("/general/speed", Configuration.speed)

		self.send('/animation/blinking-stars', 0)
		self.send('/animation/rainbow', 0)
		self.send('/animation/rainbow-mosaic', 0)
		self.send('/animation/rainbow-wave', 0)
		self.send('/animation/moving-star', 0)

		if self.animation != None:
			self.send(self.animation, 1)

		self.send('/animation/rainbow-wave/scale', Configuration.rainbow_wave_scale)
		self.send('/animation/moving-star/position', Configuration.moving_star_position)

		Configuration._hasChanged = False 

	def send(self, addr, txt):
		msg = OSC.OSCMessage(addr)
		msg.append(txt)
		logger.info("Syncing with client: " + str(msg))

		try:
			self.client.send(msg)
		except Exception, e:
			print "Exception while sending OSC message [%s]: %s" % (msg, e)

	# Brightness
	def brightness_handler(self, add, tags, args, source):
		Configuration.brightness = args[0]
		Configuration._hasChanged = True
		logger.info(str(Configuration._hasChanged))
		logger.info("brightness: " + str(Configuration.brightness))

	# Speed
	def speed_handler(self, add, tags, args, source):
		Configuration.speed = args[0]
		Configuration._hasChanged = True
		logger.info("speed: " + str(Configuration.speed))

	# Animations
	def animation_handler(self, add, tags, args, source):
		if add != Configuration.animation:
			Configuration.animation = add
			Configuration._hasChanged = True
			Configuration.animationHasChanged = True
			logger.info("animation: " + str(Configuration.animation))

	# Rainbow wave animation - scale
	def rainbow_wave_scale_handler(self, add, tags, args, source):
		Configuration.rainbow_wave_scale = args[0]

		if Configuration.rainbow_wave_scale == 0:
			Configuration.rainbow_wave_scale = 0.001

		Configuration._hasChanged = True
		logger.info("rainbow wave scale: " + str(Configuration.rainbow_wave_scale))

	# Strobe - white
	def strobe_white_handler(self, add, tags, args, source):
		self.strobe(Color['white'], args[0])

	# Strobe - yellow
	def strobe_yellow_handler(self, add, tags, args, source):
		self.strobe(Color['yellow'], args[0])

	# Strobe - orange
	def strobe_orange_handler(self, add, tags, args, source):
		self.strobe(Color['orange'], args[0])

	# Strobe - brown
	def strobe_brown_handler(self, add, tags, args, source):
		self.strobe(Color['brown'], args[0])

	# Strobe - red
	def strobe_red_handler(self, add, tags, args, source):
		self.strobe(Color['red'], args[0])

	# Strobe - pink
	def strobe_pink_handler(self, add, tags, args, source):
		self.strobe(Color['pink'], args[0])

	# Strobe - purple
	def strobe_purple_handler(self, add, tags, args, source):
		self.strobe(Color['purple'], args[0])

	# Strobe - blue
	def strobe_blue_handler(self, add, tags, args, source):
		self.strobe(Color['blue'], args[0])

	# Strobe
	def strobe(self, color, on):
		if on:
			Configuration.animation = AnimationType.Strobe
		else:
			Configuration.animation = None

		Configuration.strobe_color = color
		Configuration._hasChanged = True
		Configuration.animationHasChanged = True
		logger.info("strobe " + str(color))

	# Moving Star
	def moving_star_position_handler(self, add, tags, args, source):
		Configuration.moving_star_position = [args[0], 1.0 - args[1]]

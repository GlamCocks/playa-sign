#!/usr/bin/env python

import socket
import OSC
import re
import time
import threading
import math
import logging
import types

logger = logging.getLogger("playasign.configuration")

from structure import Singleton

# Brightness
def brightness_handler(add, tags, args, source):
	Configuration.brightness = args[0] * 100


class Configuration(object):
	__metaclass__ = Singleton

	brightness = 100.0

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
		self.thread.stop()

	def addHandlers(self):
		self.server.addMsgHandler("general/brightness", brightness_handler)

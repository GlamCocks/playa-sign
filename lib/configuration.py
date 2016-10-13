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

opc_server = '10.0.1.5', 7000
opc_client = '10.0.1.20', 9000

# Initialize the OSC server and the client.
s = OSC.OSCServer(opc_server)
c = OSC.OSCClient()
c.connect(opc_client)

# Start OSCServer
st = threading.Thread( target = s.serve_forever )
st.start()


# Brightness
def brightness_handler(add, tags, args, source):
	print "brightness" + str(args) 
	Configuration.brightness = args[0] * 100

s.addMsgHandler("/1/fader1", brightness_handler)


class Configuration(object):
	__metaclass__ = Singleton

	brightness = 100
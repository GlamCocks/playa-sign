#!/usr/bin/env python

import time 

import os
import sys
import traceback
from lib import *

fps = 30

opc_server = '10.0.1.31', 7000
opc_client = '10.0.1.20', 9000

config_server = Configuration(server=opc_server, client=opc_client)
config_server.start()

Server(config_file="config.yml")
Server().colorspace_correction = True

Server().clean()
Server().push()

stack = AnimationStack()

while True:
	stack.render()
	Server().push()
	config_server.refreshClient()
	time.sleep(1.0/float(fps))
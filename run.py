#!/usr/bin/env python

from lib import *

fps = 30

opc_server = '10.0.1.90', 7000
opc_client = '10.0.1.20', 9000

configuration = Configuration(server=opc_server, client=opc_client)
configuration.start()

Server(config_file="config.yml")
Server().colorspace_correction = True

Server().clean()
Server().push()

stack = AnimationStack()

while True:
	stack.render()
	Server().push()
	configuration.refreshClient()
	time.sleep(1.0/float(fps))

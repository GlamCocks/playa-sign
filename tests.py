#!/usr/bin/env python

import time 

from lib import *

Server(config_file="config.yml")
Server().colorspace_correction = False

Server().clean()
Server().push()

fps = 50

loop = Loop.instances[0]

animstack = AnimationStack()
animstack.add(ChasingRainbowLoop(loop=loop))
# animstack.add(RainbowLoop(loop=loop, starting_color=Color['green']))
# animstack.add(ChasingLoop(loop=loop, color=Color['red'], rotation=Rotation.Clockwise))
# animstack.add(ChasingLoop(loop=loop, color=Color['green'], rotation=Rotation.Clockwise, delay=40))
# animstack.add(ChasingLoop(loop=loop, color=Color['blue'], rotation=Rotation.Clockwise, delay=80))
# animstack.add(ChasingLoop(loop=loop, color=Color['cyan'], rotation=Rotation.CounterClockwise))
# animstack.add(ChasingLoop(loop=loop, color=Color['yellow'], rotation=Rotation.CounterClockwise, delay=40))
# animstack.add(ChasingLoop(loop=loop, color=Color['pink'], rotation=Rotation.CounterClockwise, delay=80))

while True:
	animstack.render()
	Server().push()
	time.sleep(1.0/float(fps))
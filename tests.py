#!/usr/bin/env python

import time 

from lib import *

fps=60

Server(config_file="config.yml")
Server().colorspace_correction = False
Server().brightness = 100

Server().clean()
Server().push()

loop = Loop.instances[0]

stack = AnimationStack()
stack.add(StrobeLoop(loop=loop, color=Color['white'], flash=2), delay=0, duration=100)
# animstack.add(ChasingRainbowLoop(loop=loop))
# animstack.add(RainbowLoop(loop=loop, starting_color=Color['green']))
# animstack.add(ChasingLoop(loop=loop, color=Color['red'], rotation=Rotation.Clockwise))
# animstack.add(ChasingLoop(loop=loop, color=Color['green'], rotation=Rotation.Clockwise, delay=40))
# animstack.add(ChasingLoop(loop=loop, color=Color['blue'], rotation=Rotation.Clockwise, delay=80))
# animstack.add(ChasingLoop(loop=loop, color=Color['cyan'], rotation=Rotation.CounterClockwise))
# animstack.add(ChasingLoop(loop=loop, color=Color['yellow'], rotation=Rotation.CounterClockwise, delay=40))
# animstack.add(ChasingLoop(loop=loop, color=Color['pink'], rotation=Rotation.CounterClockwise, delay=80))

while True:
	stack.render()
	Server().push()
	time.sleep(1.0/float(fps))
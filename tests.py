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
stack.add(StrobeLoop(loop=loop, color=Color['white'], flash=2), delay=1, duration=1, dismiss=True)
stack.add(ChasingRainbowLoop(loop=loop), duration=8, dismiss=True)
stack.add(StrobeLoop(loop=loop, color=Color['white'], flash=2), duration=2, dismiss=True)
stack.add(RainbowLoop(loop=loop, starting_color=Color['red']), duration=10, dismiss=True)
stack.add(ChasingLoop(loop=loop, color=Color['red'], rotation=Rotation.Clockwise))
stack.add(ChasingLoop(loop=loop, color=Color['cyan'], rotation=Rotation.CounterClockwise))
stack.add(ChasingLoop(loop=loop, color=Color['green'], rotation=Rotation.Clockwise), delay=3)
stack.add(ChasingLoop(loop=loop, color=Color['yellow'], rotation=Rotation.CounterClockwise), delay=3)
stack.add(ChasingLoop(loop=loop, color=Color['blue'], rotation=Rotation.Clockwise), delay=6)
stack.add(ChasingLoop(loop=loop, color=Color['pink'], rotation=Rotation.CounterClockwise), delay=6)

while True:
	stack.render()
	Server().push()
	time.sleep(1.0/float(fps))
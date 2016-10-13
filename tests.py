#!/usr/bin/env python

import time 

from lib import *

fps=20

Server(config_file="config.yml")
Server().colorspace_correction = True
Server().brightness = 60

Server().clean()
Server().push()

loop = Loop.instances[0]
letter = Letter[1]

stack = AnimationStack()
stack.add(RainbowLetter(letter=letter, starting_color=Color['red']), dismiss=True)
stack.add(RainbowLoop(loop=loop, starting_color=Color['orange']), dismiss=True)
# stack.add(ChasingRainbowLoop(loop=loop), dismiss=True)
# stack.add(StrobeLetter(letter=letter, color=Color['white'], flash=2), duration=0.8, dismiss=True)
# stack.add(StrobeLoop(loop=loop, color=Color['blue'], flash=2), duration=1, dismiss=True)
# stack.add(StrobeLoop(loop=loop, color=Color['white'], flash=2), duration=2, dismiss=True)
# stack.add(ChasingLoop(loop=loop, color=Color['red'], rotation=Rotation.Clockwise))
# stack.add(ChasingLoop(loop=loop, color=Color['cyan'], rotation=Rotation.CounterClockwise))
# stack.add(ChasingLoop(loop=loop, color=Color['green'], rotation=Rotation.Clockwise), delay=3)
# stack.add(ChasingLoop(loop=loop, color=Color['yellow'], rotation=Rotation.CounterClockwise), delay=3)
# stack.add(ChasingLoop(loop=loop, color=Color['blue'], rotation=Rotation.Clockwise), delay=6)
# stack.add(ChasingLoop(loop=loop, color=Color['pink'], rotation=Rotation.CounterClockwise), delay=6)

while True:
	stack.render()
	Server().push()
	time.sleep(1.0/float(fps))
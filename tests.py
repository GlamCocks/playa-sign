#!/usr/bin/env python

import time 

from sys import exit
from lib import *

fps = 100

# opc_server = '10.0.1.5', 7000
# opc_client = '10.0.1.20', 9000

# Configuration(server=opc_server, client=opc_client).start()

Server(config_file="config.yml")
Server().colorspace_correction = True

Server().clean()
Server().push()

letter = Letter[1]

stack = AnimationStack()
stack.add(BlinkingStarsLetter(letter=Letter[0], palette=ColorPalette(name='shifting palette', hue_range=[200, 220], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[1], palette=ColorPalette(name='shifting palette', hue_range=[220, 240], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[2], palette=ColorPalette(name='shifting palette', hue_range=[240, 260], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[3], palette=ColorPalette(name='shifting palette', hue_range=[260, 280], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[4], palette=ColorPalette(name='shifting palette', hue_range=[280, 300], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[5], palette=ColorPalette(name='shifting palette', hue_range=[320, 340], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[6], palette=ColorPalette(name='shifting palette', hue_range=[340, 360], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[7], palette=ColorPalette(name='shifting palette', hue_range=[0, 20], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[8], palette=ColorPalette(name='shifting palette', hue_range=[20, 40], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
# stack.add(RainbowLetter(letter=letter, starting_color=Color['red']), dismiss=True)
# stack.add(RainbowLoop(loop=loop, starting_color=Color['orange']), duration=5, dismiss=True)
# stack.add(ChasingRainbowLoop(loop=loop), duration=10, dismiss=True)
# stack.add(StrobeLetter(letter=letter, color=Color['red'], flash=2), duration=0.8, dismiss=True)
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

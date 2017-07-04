#!/usr/bin/env python

import time 

from sys import exit
from lib import *

fps = 50

# opc_server = '10.0.1.5', 7000
# opc_client = '10.0.1.20', 9000

# Configuration(server=opc_server, client=opc_client).start()

Server(config_file="config.yml")
Server().colorspace_correction = True

Server().clean()
Server().push()

letter = Letter[1]

stack = AnimationStack()

# Rainbow blinking stars
stack.add(BlinkingStarsLetter(letter=Letter[0], palette=ColorPalette(name='shifting palette', hue_range=[0, 40], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[1], palette=ColorPalette(name='shifting palette', hue_range=[40, 80], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[2], palette=ColorPalette(name='shifting palette', hue_range=[80, 120], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[3], palette=ColorPalette(name='shifting palette', hue_range=[120, 160], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[4], palette=ColorPalette(name='shifting palette', hue_range=[160, 200], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[5], palette=ColorPalette(name='shifting palette', hue_range=[200, 240], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[6], palette=ColorPalette(name='shifting palette', hue_range=[240, 280], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[7], palette=ColorPalette(name='shifting palette', hue_range=[280, 320], saturation_range=[60, 100], value_range=[60, 100]), speed=1))
stack.add(BlinkingStarsLetter(letter=Letter[8], palette=ColorPalette(name='shifting palette', hue_range=[320, 360], saturation_range=[60, 100], value_range=[60, 100]), speed=1))

# Rainbow (letters)
# stack.add(RainbowLetter(letter=Letter[0], starting_color=Color(0,100,100)))
# stack.add(RainbowLetter(letter=Letter[1], starting_color=Color(40,100,100)))
# stack.add(RainbowLetter(letter=Letter[2], starting_color=Color(80,100,100)))
# stack.add(RainbowLetter(letter=Letter[3], starting_color=Color(120,100,100)))
# stack.add(RainbowLetter(letter=Letter[4], starting_color=Color(160,100,100)))
# stack.add(RainbowLetter(letter=Letter[5], starting_color=Color(200,100,100)))
# stack.add(RainbowLetter(letter=Letter[6], starting_color=Color(240,100,100)))
# stack.add(RainbowLetter(letter=Letter[7], starting_color=Color(280,100,100)))
# stack.add(RainbowLetter(letter=Letter[8], starting_color=Color(320,100,100)))

# Blinking
# stack.add(StrobeLetter(letter=Letter[0], color=Color['red'], flash=10))
# stack.add(StrobeLetter(letter=Letter[1], color=Color['red'], flash=5))
# stack.add(StrobeLetter(letter=Letter[2], color=Color['red'], flash=2))
# stack.add(StrobeLetter(letter=Letter[3], color=Color['red'], flash=1))
# stack.add(StrobeLetter(letter=Letter[4], color=Color['red'], flash=2))
# stack.add(StrobeLetter(letter=Letter[5], color=Color['red'], flash=2))
# stack.add(StrobeLetter(letter=Letter[6], color=Color['red'], flash=2))
# stack.add(StrobeLetter(letter=Letter[7], color=Color['red'], flash=2))
# stack.add(StrobeLetter(letter=Letter[8], color=Color['red'], flash=2))

# stack.add(MovingRainbowWave(speed=5))

while True:
        stack.render()
        Server().push()
        time.sleep(1.0/float(fps))

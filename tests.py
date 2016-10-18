#!/usr/bin/env python

import time 

from lib import *

fps = 100

opc_server = '10.0.1.5', 7000
opc_client = '10.0.1.20', 9000

Configuration(server=opc_server, client=opc_client).start()

Server(config_file="config.yml")
Server().colorspace_correction = True

Server().clean()
Server().push()

loop = Loop.instances[0]
letter = Letter[1]

stack = AnimationStack()
stack.add(BlinkingStarsLetter(letter=letter, color_dimension=ColorDimension.White, speed=0.2))
# stack.add(RainbowLetter(letter=letter, starting_color=Color['red']), dismiss=True)
# stack.add(RainbowLoop(loop=loop, starting_color=Color['orange']), duration=5, dismiss=True)
# stack.add(ChasingRainbowLoop(loop=loop), duration=10, dismiss=True)
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
    try:
        stack.render()
        Server().push()
        time.sleep(1.0/float(fps))
    except (KeyboardInterrupt, SystemExit):
        Configuration.stop()
        raise

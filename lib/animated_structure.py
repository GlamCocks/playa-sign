#!/usr/bin/env python

import logging
import time

from server import Server
from structure import *

logger = logging.getLogger("playasign.structure.animated")

class ChasingLoop(object):

    def __init__(self, loop, fps):
        self.loop = loop 
        self.fps = fps

    def start(self):
        node = 0
        pixel = self.loop.nodes[node]

        while True:
            pixel.color = Color['red']
            Server().push()
            pixel.color = Color['black']

            channel = pixel.channel

            if self.loop.nodes[node].index == 0:
                index = pixel.index + 1
            else:
                index = pixel.index - 1

            if len(channel.pixels) > index and index >= 0:
                pixel = Channel[channel.index][index]
            elif len(self.loop.nodes) == node + 1:
                node = 0
                pixel = self.loop.nodes[node]
            else:
                node += 1
                pixel = self.loop.nodes[node]

            time.sleep(1.0/self.fps)

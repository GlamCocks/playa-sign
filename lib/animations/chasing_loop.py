#!/usr/bin/env python

import logging
import copy
from collections import deque

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class ChasingLoop(object):

    def __init__(self, loop, color, rotation):
        self.loop     = loop 
        self.color    = color
        self.rotation = rotation
        self.node     = 0

        self.queue = deque(maxlen=4)
        self.queue.appendleft(self.loop.nodes[self.node])

    def render(self):
        if self.rotation == Rotation.Clockwise:
            self.renderClockwise()
        else: 
            self.renderCounterClockwise()

        self.renderPixels()

    def renderClockwise(self):
        pixel = self.queue[0]
        channel = pixel.channel

        if self.loop.nodes[self.node].index == 0:
            index = pixel.index + 1
        else:
            index = pixel.index - 1

        if len(channel.pixels) > index and index >= 0:
            pixel = Channel[channel.index][index]
        else:
            self.node += 1

            if self.node == len(self.loop.nodes):
                self.node = 0

            pixel = self.loop.nodes[self.node]

        self.queue.appendleft(pixel)

    def renderCounterClockwise(self):
        pixel = self.queue[0]
        channel = pixel.channel

        if self.loop.nodes[self.node].index == 0:
            index = pixel.index - 1
        else:
            index = pixel.index + 1

        if len(channel.pixels) > index and index >= 0:
            pixel = Channel[channel.index][index]
        else: 
            self.node -= 1

            if self.node < 0:
                self.node = len(self.loop.nodes) - 1

            new_node = self.loop.nodes[self.node]
            new_channel = new_node.channel 

            if new_node.index == 0:
                pixel = Channel[new_channel.index][len(new_channel.pixels) - 1]
            else:
                pixel = Channel[new_channel.index][0]

        self.queue.appendleft(pixel)

    def renderPixels(self):
        values = [100, 60, 30, 0]

        for i in xrange(len(self.queue)):
            v = values[i]
            pixel = self.queue[i]
            pixel.color = copy.deepcopy(self.color) 
            pixel.color.v = v 
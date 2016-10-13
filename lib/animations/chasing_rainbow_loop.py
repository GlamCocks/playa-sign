#!/usr/bin/env python

import logging
import time
import copy

from ..structure import *

logger = logging.getLogger("playasign.animations")

class ChasingRainbowLoop(object):

    def __init__(self, loop):
        self.loop     = loop 

        self._pixels = []
        self.orderPixels()
        self._deltaHue = 360.0 / float(len(self._pixels))
        self._origin = 0.0

    def orderPixels(self):
        node = 0
        pixel = self.loop.nodes[node]

        while True:
            self._pixels.append(pixel)
            channel = pixel.channel

            if self.loop.nodes[node].index == 0:
                index = pixel.index + 1
            else:
                index = pixel.index - 1

            if len(channel.pixels) > index and index >= 0:
                pixel = Channel[channel.index][index]
            else:
                node += 1

                if node == len(self.loop.nodes):
                    break

                pixel = self.loop.nodes[node]

    def render(self):
        self.renderPixels()

    def renderPixels(self):
        hue = self._origin

        for pixel in self._pixels:
            pixel.color = Color(hue, 100, 100)
            hue += self._deltaHue

        self._origin += self._deltaHue
        self._origin %= 360
#!/usr/bin/env python

import logging
import math
import copy

from ..structure import *

logger = logging.getLogger("playasign.animations")


class MovingLightLetter(object):

    def __init__(self, letter, palette, speed=1):
        self.letter = letter 
        self.palette = palette
        self.speed = speed

        self.y = self.x = self.start = -0.2
        self.end = 1.2

    def render(self):
        self.x += self.speed / 100.0
        self.y += self.speed / 100.0

        if self.x > self.end:
            self.x = self.start

        if self.y > self.end:
            self.y = self.start

        self.renderPixels()

    def renderPixels(self):
        color = self.palette.nextColor()

        for channel in self.letter.channels:
            for pixel in channel.pixels:
                if pixel.x != None and pixel.y != None:
                    diff_x = 1.0 / (math.cosh(pixel.x - self.x)**200) 
                    diff_y = 1.0 / (math.cosh(pixel.y - self.y)**200)
                    pixel.color = copy.deepcopy(color)
                    pixel.color.v = diff_x * 100
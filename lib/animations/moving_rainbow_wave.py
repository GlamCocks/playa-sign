#!/usr/bin/env python

import logging
import math
import copy

from ..structure import *

logger = logging.getLogger("playasign.animations")


class MovingRainbowWave(object):

    def __init__(self, speed=1):
        self.speed = speed

        self.y = self.x = self.start = 0
        self.end = 1.0

    def render(self):
        self.x += 0.001
        self.y += self.speed / 100.0

        if self.x > self.end:
            self.x = self.start

        if self.y > self.end:
            self.y = self.start

        self.renderPixels()

    def renderPixels(self):
        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                diff_x = self.x * 360
                pixel.color = copy.deepcopy(Color['white'])
                pixel.color.h = 40
                # diff_y = 1.0 / (math.cosh(pixel.y - self.y)**200)
                # pixel.color = copy.deepcopy(color)
                # pixel.color.v = diff_x * 100
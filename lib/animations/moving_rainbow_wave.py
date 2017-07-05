#!/usr/bin/env python

import logging
import math
import copy

from ..structure import *

logger = logging.getLogger("playasign.animations")


class MovingRainbowWave(object):

    def __init__(self, scale=1, speed=1):
        self.speed = speed
        self.clock = 0.0
        self.scale = scale

        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                pixel.color = Color['white']

    def render(self):
        self.clock += self.speed / (self.scale * 360)

        if self.clock >= 1.0 / self.scale:
            self.clock = 0.0

        self.renderPixels()

    def renderPixels(self):
        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                pixel.color.h = (self.clock + pixel.x + pixel.y * 0.3) * (self.scale * 360)
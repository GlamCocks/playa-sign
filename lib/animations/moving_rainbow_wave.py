#!/usr/bin/env python

import logging
import math
import copy

from ..structure import *
from ..configuration import *

logger = logging.getLogger("playasign.animations")


class MovingRainbowWave(object):

    def __init__(self):
        self.clock = 0.0

        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                pixel.color = Color['red']

    def render(self):
        self.clock += (Configuration.speed * 5) / (Configuration.rainbow_wave_scale * 360)

        if self.clock >= 1.0 / Configuration.rainbow_wave_scale:
            self.clock = 0.0

        self.renderPixels()

    def renderPixels(self):
        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                pixel.color.h = (self.clock + pixel.x + pixel.y * 0.3) * (Configuration.rainbow_wave_scale * 360)
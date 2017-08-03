#!/usr/bin/env python

import logging
import random 
import math

from ..structure import *
from ..configuration import *

logger = logging.getLogger("playasign.animations")

class RainbowMosaicPixel(object):

    def __init__(self, pixel, palette):
        self.pixel = pixel 
        self.palette = palette
        self.duration = random.uniform(10.0, 1000.0) / (Configuration.speed * 5)
        self.pixel.color = self.palette.randomColor()

    def next(self):
        if self.duration <= 0.0:
            self.pixel.color = self.palette.randomColor()
            self.duration = random.uniform(10.0, 1000.0) / (Configuration.speed * 5)

        self.duration -= 1


class RainbowMosaic(object):

    def __init__(self, letter, palette):
        self.letter = letter 
        self.palette = palette
        self._pixels = []
        self.initPixels()

    def render(self):
        self.renderPixels()

    def renderPixels(self):
        for pixel in self._pixels:
            pixel.next()

    def initPixels(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                self._pixels.append(RainbowMosaicPixel(pixel, self.palette))

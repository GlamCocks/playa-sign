#!/usr/bin/env python

import logging
import random 
import math

from ..structure import *

logger = logging.getLogger("playasign.animations")

class RainbowMosaicPixel(object):

    def __init__(self, pixel, palette, speed):
        self.pixel = pixel 
        self.speed = speed
        self.palette = palette
        self.duration = random.uniform(10.0, 1000.0) / self.speed
        self.pixel.color = self.palette.randomColor()

    def next(self):
        if self.duration <= 0.0:
            self.pixel.color = self.palette.randomColor()
            self.duration = random.uniform(10.0, 1000.0) / self.speed

        self.duration -= 1


class RainbowMosaic(object):

    def __init__(self, letter, palette, speed=1):
        self.letter = letter 
        self.speed = speed
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
                self._pixels.append(RainbowMosaicPixel(pixel, self.palette, self.speed))

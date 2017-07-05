#!/usr/bin/env python

import logging
import random 
import math

from ..structure import *

logger = logging.getLogger("playasign.animations")

class BlinkingStar(object):

    def __init__(self, pixel, palette):
        self.pixel = pixel 
        self.palette = palette
        self.pixel.color = palette.randomColor()
        
        random_move = random.uniform(-5, 5)
        self.move = -0.5 if math.fabs(random_move < 0.5) else random_move

    def next(self, speed=1, delta_hue=0):
        if self.pixel.color.v == 0 and random.randint(0,1) == 0:
            self.move = random.uniform(0.5, 5)
            self.pixel.color = self.palette.randomColor()
            self.pixel.color.v = 0
            self.pixel.color.h += delta_hue
        elif self.pixel.color.v == 100:
            self.move = random.uniform(-5, -0.5)

        self.pixel.color.v += self.move

class BlinkingStarsLetter(object):

    def __init__(self, letter, palette, speed=1):
        self.letter = letter 
        self.speed = speed
        self.palette = palette
        self._stars = []
        self._clock = 0
        self.initStars()

    def render(self):
        self._clock = (self._clock + 0.05 * self.speed) % 360
        self.renderPixels()

    def renderPixels(self):
        for star in self._stars:
            star.next(speed=self.speed, delta_hue=self._clock)

    def initStars(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                self._stars.append(BlinkingStar(pixel, self.palette))

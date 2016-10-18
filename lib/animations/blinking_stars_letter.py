#!/usr/bin/env python

import logging
import random 

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class BlinkingStar(object):

    def __init__(self, pixel, color_dimension):

        if color_dimension == ColorDimension.Colors:
            self.s = 100
        else:
            self.s = 0

        self.pixel = pixel 
        self.pixel.color = Color(random.randint(0, 360), self.s, random.randint(0, 100))
        self.move = random.sample([-2, -1.5, -1, 0.2, 0.5, 1], 1)[0]

    def next(self, speed = 1):
        if self.pixel.color.v == 0 and random.randint(0, 1000) == 0:
            self.move = random.sample([0.5, 0.8, 1], 1)[0] * speed
            self.pixel.color = Color(random.randint(0, 360), self.s, 30)
        elif self.pixel.color.v == 100 and random.randint(0, 20) == 0:
            self.move = random.sample([-4, -3, -2], 1)[0] * speed

        self.pixel.color.v += self.move


class BlinkingStarsLetter(object):

    def __init__(self, letter, color_dimension = ColorDimension.Colors, speed=1):
        self.letter = letter 
        self.speed = speed
        self.color_dimension = color_dimension
        self._stars = []
        self.initStars()

    def render(self):
        self.renderPixels()

    def renderPixels(self):
        for star in self._stars:
            star.next(speed=self.speed)

    def initStars(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                self._stars.append(BlinkingStar(pixel, self.color_dimension))

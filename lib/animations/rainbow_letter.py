#!/usr/bin/env python

import logging

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class RainbowLetter(object):

    def __init__(self, letter, starting_color):
        self.letter = letter 
        self.color  = starting_color

    def render(self):
        self.color.h += 1
        self.renderPixels()

    def renderPixels(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                pixel.color = self.color  
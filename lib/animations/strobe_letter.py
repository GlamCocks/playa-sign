#!/usr/bin/env python

import logging

from ..structure import *
from ..configuration import *

logger = logging.getLogger("playasign.animations")

class StrobeLetter(object):

    def __init__(self, letter):
        self.letter = letter 
        self._clock = 0
        self._offColor = Color['black']

        if Configuration.strobe_color != None:
            self._onColor = Configuration.strobe_color 
        else: 
            self._onColor = Color['black']

        for channel in self.letter.channels:
            for pixel in channel.pixels:
                pixel.color = self._offColor

    def render(self):
        self._clock += 1
        self._clock %= 5

        self.renderPixels()

    def renderPixels(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                if self._clock == 0:
                    pixel.color = color
                else:
                    pixel.color = self._offColor

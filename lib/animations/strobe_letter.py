#!/usr/bin/env python

import logging

from ..structure import *
from ..configuration import *

logger = logging.getLogger("playasign.animations")

class StrobeLetter(object):

    def __init__(self, letter):
        self.letter = letter 
        self._clock = 0

    def render(self):
        self._clock += 1
        self._clock %= 5

        self.renderPixels()

    def renderPixels(self):
        color = Color['black']

        if Configuration.strobe_color != None:
            color = Configuration.strobe_color 

        for channel in self.letter.channels:
            for pixel in channel.pixels:
                if self._clock == 0:
                    pixel.color = color
                else:
                    pixel.color = Color['black']

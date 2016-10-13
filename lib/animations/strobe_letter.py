#!/usr/bin/env python

import logging
import time
import copy

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class StrobeLetter(object):

    def __init__(self, letter, color, flash=1):
        self.letter = letter 
        self.color  = color
        self.flash  = flash

        self._clock = 0

    def render(self):
        self._clock += 1
        self._clock %= self.flash + 1

        self.renderPixels()

    def renderPixels(self):
        for channel in self.letter.channels:
            for pixel in channel.pixels:
                if self._clock == 0:
                    pixel.color = self.color  
                else:
                    pixel.color = Color['black']
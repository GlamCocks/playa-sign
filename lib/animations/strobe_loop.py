#!/usr/bin/env python

import logging
import time
import copy

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class StrobeLoop(object):

    def __init__(self, loop, color, flash=1):
        self.loop  = loop 
        self.color = color
        self.flash = flash

        self._clock = 0

    def render(self):
        self._clock += 1
        self._clock %= self.flash + 1

        self.renderPixels()

    def renderPixels(self):
        for node in self.loop.nodes:
            for pixel in node.channel.pixels:
                if self._clock == 0:
                    pixel.color = self.color  
                else:
                    pixel.color = Color['black']
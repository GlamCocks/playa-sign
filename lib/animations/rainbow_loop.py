#!/usr/bin/env python

import logging
import time
import copy
from collections import deque

from ..structure import *
from enums import *

logger = logging.getLogger("playasign.animations")

class RainbowLoop(object):

    def __init__(self, loop, starting_color):
        self.loop  = loop 
        self.color = starting_color

    def render(self):
        self.color.h += 1
        self.renderPixels()

    def renderPixels(self):
        for node in self.loop.nodes:
            for pixel in node.channel.pixels:
                pixel.color = self.color  
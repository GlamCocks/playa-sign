#!/usr/bin/env python

import logging
import math
import copy

from ..structure import *
from ..configuration import *

logger = logging.getLogger("playasign.animations")


class MovingStar(object):

    def __init__(self):
        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                pixel.color = Color['black']

    def render(self):
        self.renderPixels()

    def renderPixels(self):
        position = Configuration.moving_star_position

        for pixel in Pixel.instances:
            if pixel.x != None and pixel.y != None:
                if math.fabs(pixel.x - position[0]) < 0.01 and math.fabs(pixel.y - position[1]) < 0.03:
                    pixel.color = Color['red']
                else: 
                    pixel.color = Color['black']
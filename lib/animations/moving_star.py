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
                d = math.sqrt(math.pow(pixel.x - position[0], 2) + math.pow(pixel.y - position[1], 2))
                print(str(d))
                # print(str(math.pow(1-d, 100)))
                pixel.color = Color(0, 100, math.pow(d, 50))

#!/usr/bin/env python

import logging

from pixel import *

logger = logging.getLogger("playasign.structure.Channel")


class Channel(object):

    def __init__(self, index, numberOfPixels, type, colorspace):
        self.index      = index
        self.pixels     = []
        self.type       = type
        self.colorspace = colorspace

        for i in range(numberOfPixels):
            self.pixels.append(Pixel(i))

        logger.info("new channel created: " + str(self))

    def __repr__(self):
        return "channel #" + str(self.index) + " (" + str(self.type) + " - " + str(len(self.pixels)) + " pixels - " + str(self.colorspace) +")"
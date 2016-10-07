#!/usr/bin/env python

import logging

logger = logging.getLogger("playasign.structure.Pixel")


class Pixel(object):

    def __init__(self, index):
    	self.index = index
    	self.color = [0,0,0]

        logger.info("new pixel created: " + str(self))

    def __repr__(self):
        return "pixel #" + str(self.index) + " color " + str(self.color)
#!/usr/bin/env python

import logging

logger = logging.getLogger("playasign.structure.Letter")


class Letter(object):

    def __init__(self, index, character, width, height):
        self.index = index
        self.character = character
        self.channels = []
        self.width = 0
        self.height = 0

        logger.info("new letter created: " + str(self))

    def __repr__(self):
        return "letter " + str(self.character) + " (#" + str(self.index) + ")"
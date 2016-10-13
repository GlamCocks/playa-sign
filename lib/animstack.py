#!/usr/bin/env python

import logging

from structure import *

logger = logging.getLogger("playasign.animstack")

class AnimationStack(object):
    def __init__(self):
        self.__animations = []
        self.animated = True
        logger.info("new animation stack created: " + str(self))

    def add(self, animation):
        self.__animations.append(animation)
        logger.info("new animation added to the stack: " + str(animation))

    def render(self):
        if self.animated == False:
            return 

        for animation in self.__animations:
            animation.render()

    def __repr__(self):
        return "animation stack (" + str(len(self.__animations)) + " animations)"
#!/usr/bin/env python

import logging
import time 

from ..structure import *
from ..server import Server

logger = logging.getLogger("playasign.animations")

class Animation(object):
    def __init__(self, animation):
        self.animation = animation 

class AnimationStack(object):
    def __init__(self):
        self.__animations = []
        logger.info("new animation stack created: " + str(self))

    def clear(self):
        self.__animations = []
        
        Server().clean()
        logger.info("animation stack cleared")

    def add(self, animation):
        new_animation = Animation(animation=animation)
        self.__animations.append(new_animation)

        logger.info("new animation added to the stack: " + str(animation))

    def render(self):
        for animation in self.__animations:
            animation.animation.render()

    def __repr__(self):
        return "animation stack (" + str(len(self.__animations)) + " active)"
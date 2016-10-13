#!/usr/bin/env python

import logging
import time 

from ..structure import *
from ..server import Server

logger = logging.getLogger("playasign.animations")

class Animation(object):
    def __init__(self, animation, start, end, dismiss):
        self.animation = animation 
        self.start     = start
        self.end       = end 
        self.dismiss   = dismiss

class AnimationStack(object):
    def __init__(self):
        self.__current_animations = []
        self.__delayed_animations = []

        self.animated = True
        logger.info("new animation stack created: " + str(self))

    def add(self, animation, delay=0, duration=None, dismiss=False):
        start = time.time() + delay

        if duration == None:
            end = time.time() + 1000000000000000
        else:
            end = start + duration

        print str(start) + "  - -  " + str(end)
        
        new_animation = Animation(animation=animation, start=start, end=end, dismiss=dismiss)

        logger.info("new animation added to the stack: " + str(animation))

    def render(self):
        if self.animated == False:
            return 

        for animation in self.__current_animations:
            animation.animation.render()

            if animation.end <= time.time():
                self.__current_animations.remove(animation)

                if animation.dismiss == True:
                    Server().clean()

        for animation in self.__delayed_animations:
            if animation.start <= time.time():
                self.__current_animations.append(animation)
                self.__delayed_animations.remove(animation)

    def __repr__(self):
        return "animation stack (active: " + str(len(self.__current_animations)) + " - queue: + " + str(len(self.__delayed_animations)) + ")"
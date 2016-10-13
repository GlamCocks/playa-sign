#!/usr/bin/env python

import logging

from ..structure import *
from ..server import Server

logger = logging.getLogger("playasign.animations")

class Animation(object):
    def __init__(self, animation, delay, duration, dismiss):
        self.animation = animation 
        self.delay     = delay
        self.duration  = duration 
        self.dismiss   = dismiss

class AnimationStack(object):
    def __init__(self):
        self.__current_animations = []
        self.__delayed_animations = []

        self.animated = True
        logger.info("new animation stack created: " + str(self))

    def add(self, animation, delay=0, duration=-1, dismiss=False):
        new_animation = Animation(animation=animation, delay=delay, duration=duration, dismiss=dismiss)

        if delay == 0:
            self.__current_animations.append(new_animation)
        else:
            self.__delayed_animations.append(new_animation)

        logger.info("new animation added to the stack: " + str(animation))

    def render(self):
        if self.animated == False:
            return 

        for animation in self.__current_animations:
            animation.animation.render()

            if animation.duration == -1:
                continue

            animation.duration -= 1

            if animation.duration == 0:
                self.__current_animations.remove(animation)

                if animation.dismiss == True:
                    Server().clean()

        for animation in self.__delayed_animations:
            animation.delay -= 1

            if animation.delay == 0:
                self.__current_animations.append(animation)
                self.__delayed_animations.remove(animation)

    def __repr__(self):
        return "animation stack (active: " + str(len(self.__current_animations)) + " - queue: + " + str(len(self.__delayed_animations)) + ")"
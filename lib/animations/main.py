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
        self.__queued_animations  = []

        self.hidden = False

        self._last_animation_end = None

        logger.info("new animation stack created: " + str(self))

    def clear(self):
        self.__current_animations = []
        self.__queued_animations  = []
        
        Server().clean()
        logger.info("animation stack cleared")

    def add(self, animation, delay=0, duration=None, dismiss=False):
        if self._last_animation_end == None:
            start = time.time() + delay
        else:  
            start = self._last_animation_end + delay

        if duration == None:
            end = time.time() + 1000000000000000
        else:
            end = start + duration
            self._last_animation_end = end

        new_animation = Animation(animation=animation, start=start, end=end, dismiss=dismiss)
        self.__queued_animations.append(new_animation)

        logger.info("new animation added to the stack: " + str(animation))

    def render(self):
        if self.hidden == True:
            return 

        for animation in self.__current_animations:
            animation.animation.render()

            if animation.end <= time.time():
                self.__current_animations.remove(animation)

                if len(self.__current_animations) == 0:
                    self._last_animation_end = None

                if animation.dismiss == True:
                    Server().clean()

        for animation in self.__queued_animations:
            if animation.start <= time.time():
                self.__current_animations.append(animation)
                self.__queued_animations.remove(animation)

    def __repr__(self):
        return "animation stack (active: " + str(len(self.__current_animations)) + " - queue: + " + str(len(self.__queued_animations)) + ")"
#!/usr/bin/env python

import logging
import pixel

logger = logging.getLogger("playasign.structure")


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class MetaLetter(type):

    def __getitem__(cls, index):
        for letter in Letter.instances:
            if letter.index == index:
                return letter


class Letter(object):
    instances = []

    def __init__(self, index, character, width, height):
        self.index     = index
        self.character = character
        self.channels  = []
        self.loops     = []
        self.width     = 0
        self.height    = 0

        Letter.instances.append(self)

        logger.info("new letter created: " + str(self))

    def __repr__(self):
        return "letter " + str(self.character) + " (#" + str(self.index) + ")"


class MetaChannel(type):

    def __getitem__(cls, index):
        return Channel.instances[index]


class Channel(object):
    __metaclass__ = MetaChannel

    instances = []

    def __init__(self, index, numberOfPixels, type, colorspace):
        self.index      = index
        self.pixels     = []
        self.type       = type
        self.colorspace = colorspace

        for i in range(numberOfPixels):
            self.pixels.append(Pixel(self, i))

        Channel.instances.append(self)

        logger.info("new channel created: " + str(self))

    def __getitem__(self, index):
        if index < len(self.pixels):
            return self.pixels[index]
        else:
            return EmptyPixel()

    def __repr__(self):
        return "channel #" + str(self.index) + " (" + str(self.type) + " - " + str(len(self.pixels)) + " pixels - " + str(self.colorspace) +")"


class MetaPixel(type):

    def __getitem__(cls, index):
        channel = int(index / 64)
        pixel   = index % 64
        return Channel[channel][pixel]


class Pixel(object):
    __metaclass__ = MetaPixel

    def __init__(self, channel, index):
        self.channel = channel
        self.index   = index
        self.color   = [0,0,0]

        logger.info("new pixel created: " + str(self))

    def __repr__(self):
        return "pixel #" + str(self.channel.index * 64 + self.index) + " (" + str(self.channel.index) +"[" + str(self.index) + "]): color " + str(self.color)


class EmptyPixel(object):
    __metaclass__ = Singleton

    color = [0,0,0]        

    def __repr__(self):
        return "empty pixel"


class MetaLoop(type):

    def __getitem__(cls, index):
        return Loop.instances[index]


class Loop(object):
    __metaclass__ = MetaLoop

    instances = []

    def __init__(self):
        self.nodes = []
        
        Loop.instances.append(self)

        logger.info("new loop created: " + str(self))

    def __repr__(self):
        return "loop with nodes: " + str(self.nodes) 
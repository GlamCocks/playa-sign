#!/usr/bin/env python

import logging
import colorsys

logger = logging.getLogger("playasign.structure")


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class MetaColor(type):

    def __getitem__(cls, color):
        switcher = {
            'white':  Color(0,0,100),
            'black':  Color(0,0,0),
            'red':    Color(0,100,100),
            'green':  Color(120,100,100),
            'blue':   Color(240,100,100),
            'yellow': Color(60,100,100),
            'cyan':   Color(180,100,100),
            'pink':   Color(300,100,100),
            'orange': Color(30,100,100),
            'purple': Color(270,100,100),
        }

        return switcher.get(color, None)


class Color(object):
    __metaclass__ = MetaColor

    def __init__(self, hue, saturation, value):
        self._h = hue % 360
        self._s = max(min(saturation, 100), 0)
        self._v = max(min(value, 100), 0) 

    def set_h(self, value):
        self._h = value % 360

    def get_h(self):
        return self._h

    def set_s(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self._s = value 

    def get_s(self):
        return self._s

    def set_v(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self._v = value 

    def get_v(self):
        return self._v

    h = property(get_h, set_h)
    s = property(get_s, set_s)
    v = property(get_v, set_v)

    def raw(self, colorspace, brightness):
        rgb = colorsys.hsv_to_rgb(self._h / 360.0, self._s / 100.0, self._v / 100.0 * float(brightness) / 100.0)

        if colorspace == 'RGB':
            return [int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)]
        elif colorspace == 'GRB':
            return [int(rgb[1] * 255), int(rgb[0] * 255), int(rgb[2] * 255)]
        else:
            return [self._h, self._s, self._v]


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
        self.color   = Color['black']

        logger.info("new pixel created: " + str(self))

    def __repr__(self):
        return "pixel #" + str(self.channel.index * 64 + self.index) + " (" + str(self.channel.index) +"[" + str(self.index) + "]): color " + str(self.color)


class EmptyPixel(object):
    __metaclass__ = Singleton

    __color = Color['black']      

    @property
    def color(self):
        return self.__color 

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
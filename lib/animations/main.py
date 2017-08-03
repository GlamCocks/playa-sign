#!/usr/bin/env python

import logging
import time 

from ..structure import *
from ..server import Server
from ..configuration import * 
from blinking_stars_letter import *
from rainbow_letter import *
from rainbow_mosaic import *
from moving_rainbow_wave import *
from strobe_letter import *
from moving_star import *

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
        if Configuration.animationHasChanged == True:
            self.clear()

            if Configuration.animation == AnimationType.Rainbow:
                self.animationRainbow()
            if Configuration.animation == AnimationType.RainbowWave:
                self.animationRainbowWave()
            if Configuration.animation == AnimationType.RainbowMosaic:
                self.animationRainbowMosaic()
            if Configuration.animation == AnimationType.BlinkingStars:
                self.animationBlinkingStars()
            if Configuration.animation == AnimationType.Strobe:
                self.animationStrobe()
            if Configuration.animation == AnimationType.MovingStar:
                self.animationMovingStar()

            Configuration.animationHasChanged = False

        for animation in self.__animations:
            animation.animation.render()

    def __repr__(self):
        return "animation stack (" + str(len(self.__animations)) + " active)"

    def animationStrobe(self):
        self.add(StrobeLetter(letter=Letter[0]))
        self.add(StrobeLetter(letter=Letter[1]))
        self.add(StrobeLetter(letter=Letter[2]))
        self.add(StrobeLetter(letter=Letter[3]))
        self.add(StrobeLetter(letter=Letter[4]))
        self.add(StrobeLetter(letter=Letter[5]))
        self.add(StrobeLetter(letter=Letter[6]))
        self.add(StrobeLetter(letter=Letter[7]))
        self.add(StrobeLetter(letter=Letter[8]))

    def animationRainbowWave(self):
        self.add(MovingRainbowWave())

    def animationMovingStar(self):
        self.add(MovingStar())

    def animationRainbowMosaic(self):
        self.add(RainbowMosaic(letter=Letter[0], palette=ColorPalette(name='shifting palette', hue_range=[0, 40], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[1], palette=ColorPalette(name='shifting palette', hue_range=[40, 80], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[2], palette=ColorPalette(name='shifting palette', hue_range=[80, 120], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[3], palette=ColorPalette(name='shifting palette', hue_range=[120, 160], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[4], palette=ColorPalette(name='shifting palette', hue_range=[160, 200], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[5], palette=ColorPalette(name='shifting palette', hue_range=[200, 240], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[6], palette=ColorPalette(name='shifting palette', hue_range=[240, 280], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[7], palette=ColorPalette(name='shifting palette', hue_range=[280, 320], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(RainbowMosaic(letter=Letter[8], palette=ColorPalette(name='shifting palette', hue_range=[320, 360], saturation_range=[60, 100], value_range=[60, 100])))

    def animationRainbow(self):
        self.add(RainbowLetter(letter=Letter[0], starting_color=Color(0,100,100)))
        self.add(RainbowLetter(letter=Letter[1], starting_color=Color(40,100,100)))
        self.add(RainbowLetter(letter=Letter[2], starting_color=Color(80,100,100)))
        self.add(RainbowLetter(letter=Letter[3], starting_color=Color(120,100,100)))
        self.add(RainbowLetter(letter=Letter[4], starting_color=Color(160,100,100)))
        self.add(RainbowLetter(letter=Letter[5], starting_color=Color(200,100,100)))
        self.add(RainbowLetter(letter=Letter[6], starting_color=Color(240,100,100)))
        self.add(RainbowLetter(letter=Letter[7], starting_color=Color(280,100,100)))
        self.add(RainbowLetter(letter=Letter[8], starting_color=Color(320,100,100)))

    def animationBlinkingStars(self):
        self.add(BlinkingStarsLetter(letter=Letter[0], palette=ColorPalette(name='shifting palette', hue_range=[0, 40], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[1], palette=ColorPalette(name='shifting palette', hue_range=[40, 80], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[2], palette=ColorPalette(name='shifting palette', hue_range=[80, 120], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[3], palette=ColorPalette(name='shifting palette', hue_range=[120, 160], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[4], palette=ColorPalette(name='shifting palette', hue_range=[160, 200], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[5], palette=ColorPalette(name='shifting palette', hue_range=[200, 240], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[6], palette=ColorPalette(name='shifting palette', hue_range=[240, 280], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[7], palette=ColorPalette(name='shifting palette', hue_range=[280, 320], saturation_range=[60, 100], value_range=[60, 100])))
        self.add(BlinkingStarsLetter(letter=Letter[8], palette=ColorPalette(name='shifting palette', hue_range=[320, 360], saturation_range=[60, 100], value_range=[60, 100])))

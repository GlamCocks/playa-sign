#!/usr/bin/env python

from ..structure import Singleton

class AnimationType:
	__metaclass__ = Singleton
	
	BlinkingStars = "/animation/blinking-stars"
	Rainbow = "/animation/rainbow"
	RainbowMosaic = "/animation/rainbow-mosaic"
	RainbowWave = "/animation/rainbow-wave"
	Strobe = "/animation/strobe"
	MovingStar = "/animation/moving-star"

#!/usr/bin/env python

import yaml
import logging
import opc 

from structure import *
from configuration import *

logger = logging.getLogger("playasign.server")

class Server(object):
    __metaclass__ = Singleton

    def __init__(self, config_file):
        self.configure(config_file=config_file)

        self.colorspace_correction = True

        logger.info("new server created: " + str(self))

    def configure(self, config_file):
        config = None

        with open(config_file, 'r') as f:
            config = yaml.load(f)

        logger.info("loading configuration: " + config['name'])

        # OPC client
        self.client = opc.Client(str(config['server']['ip']) + ':' + str(config['server']['port']))

        logger.info("connected to OPC client: " + str(self.client))

        # Channels
        for channel in config['channels']:
            Channel(index=channel['index'], numberOfPixels=channel['pixels'], type=channel['type'], colorspace=channel['colorspace'])

        # Letters
        for letter in config['letters']:
            new_letter = Letter(index=letter['index'], character=letter['character'], width=letter['width'], height=letter['height'])

            for i in letter['channels']:
                new_letter.channels.append(Channel[i])
                logger.info("channel " + str(Channel[i]) + " added to letter " + str(new_letter))

            # Loops 
            for loop in letter['loops']:
                new_loop = Loop()

                for node in loop:
                    pixel = Channel[node['channel']][node['pixel']]
                    new_loop.nodes.append(pixel)

                new_letter.loops.append(new_loop)

    def clean(self):
        for channel in Channel.instances:
            for pixel in channel.pixels:
                pixel.color = Color['black']

        logger.info("pixels reset to black")

    def push(self):
        pixels = []
        
        for channel in Channel.instances:
            for x in range(64):
                if self.colorspace_correction == True:
                    colorspace = channel.colorspace
                else:
                    colorspace = "RGB"

                pixels.append(channel[x].color.raw(colorspace=colorspace, brightness=Configuration.brightness))

        self.client.put_pixels(pixels, channel=0)

        logger.info("pushing new frame")

    def __repr__(self):
        return "server (" + str(len(Channel.instances)) + " channels)"
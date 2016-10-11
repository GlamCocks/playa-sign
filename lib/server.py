#!/usr/bin/env python

from channel import *
from letter import *
from opc import *

import yaml
import logging
import color_utils

logger = logging.getLogger("playasign.structure.Server")


class Server(object):

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
        self.client = Client(str(config['server']['ip']) + ':' + str(config['server']['port']))

        logger.info("connected to OPC client: " + str(self.client))

        # Channels
        self.channels = []

        for channel in config['channels']:
            new_channel = Channel(index=channel['index'], numberOfPixels=channel['pixels'], type=channel['type'], colorspace=channel['colorspace'])
            self.channels.append(new_channel)

        # Letters
        self.letters = []

        for letter in config['letters']:
            new_letter = Letter(index=letter['index'], character=letter['character'], width=letter['width'], height=letter['height'])

            for channel_index in letter['channels']:
                for channel in self.channels:
                    if channel.index != channel_index:
                        continue 

                    new_letter.channels.append(channel)
                    logger.info("channel " + str(channel) + " added to letter " + str(new_letter))

            self.letters.append(new_letter)

    def push(self):
        pixels = []
        
        for channel in self.channels:
            for i in range(64):
                color = [0,0,0]

                if i < len(channel.pixels):
                    color = channel.pixels[i].color 

                if self.colorspace_correction == True:
                    color = color_utils.to_RGB(color, channel.colorspace)

                pixels.append(color)

        self.client.put_pixels(pixels, channel=0)

        logger.info("pushing new frame")

    def __repr__(self):
        return "server (" + str(len(self.channels)) + " channels)"
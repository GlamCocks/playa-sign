import logging
import logging.config
import color_utils

from structure          import *
from animated_structure import *
from server             import Server

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
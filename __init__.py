import logging
import logging.config

from lib import *
from opc import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
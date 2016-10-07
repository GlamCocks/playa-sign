import logging
import logging.config

from opc import *
from structure import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
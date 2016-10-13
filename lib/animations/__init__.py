import logging
import logging.config

from chasing_loop import *
from enums 		  import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
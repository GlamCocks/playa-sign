import logging
import logging.config

from enums                import *
from main                 import *
from chasing_loop         import *
from rainbow_loop         import *
from chasing_rainbow_loop import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
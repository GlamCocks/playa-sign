import logging
import logging.config

from enums                 import *
from main                  import *
from blinking_stars_letter import *
from moving_rainbow_wave   import *
from rainbow_letter        import *
from strobe_letter         import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
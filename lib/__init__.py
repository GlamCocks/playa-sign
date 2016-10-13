import logging
import logging.config

from structure     import *
from animations    import *
from server        import Server
from configuration import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("playasign")
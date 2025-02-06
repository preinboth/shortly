#######################
# 	Logging Levels:
#
#   Level  		|  Numeric value
#   -----  		|  -------------
#   Critical  |  50
#   Error		  |  40
#   Warning	  |  30
#   Info		  |  20
#   Debug		  |  10
#   NotSet	  |  0
#######################

import logging

from . import handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# -------- add Handlers ---------
logger.addHandler(handlers.file_handler)
logger.addHandler(handlers.stream_handler)
# -------------------------

# Test

# ---------------------------------------------------------------- #
# logger.debug("Debug")
# logger.info("Info")
# logger.warning("Warning")
# logger.error("Error")
# logger.critical("Critical")

# print(logger.level)

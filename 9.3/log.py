from loguru import logger

logger.add ('record.log')

logger.info ("INFO")
logger.debug ("DEBUG")
logger.warning ("WARNING")
logger.error ("ERROR")
logger.critical ("CRITICAL")
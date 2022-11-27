import logging
import requests

import bot.config as cfg

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)

print("Hello World")

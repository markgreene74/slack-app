import logging
import os

# logging config
DEBUG_MODE = True if os.environ.get("SLACK_BOT_DEBUG") else False
log_level = logging.DEBUG if DEBUG_MODE else logging.INFO
log_formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s [%(name)s]")
log_formatter.datefmt = "%Y/%m/%d %H:%M:%S"
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(log_formatter)

# slack tokens
SLK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

# log some useful info
logger = logging.getLogger(__name__)
logger.setLevel(log_level)
logger.addHandler(ch)

_debug_msg = f"{SLK_BOT_TOKEN[-4:]=}, {SLK_APP_TOKEN[-4:]=}"
logger.debug(_debug_msg)

logger.info(f"Config completed ({DEBUG_MODE=})")

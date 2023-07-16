import logging
import os
from pathlib import Path

# ### logging config ###

# logfile
log_file_name = "slack-app.log"
# TODO need to revisit after the config is moved
#      to a toml file https://github.com/markgreene74/slack-app/issues/21
if (log_file_path := Path("/var/log/slack-app")).is_dir():
    pass
else:
    log_file_path = Path("./logs")
    log_file_path.mkdir(parents=True, exist_ok=True)
log_file = log_file_path / log_file_name

# level
DEBUG_MODE = True if os.environ.get("SLACK_BOT_DEBUG") else False
log_level = logging.DEBUG if DEBUG_MODE else logging.INFO

# formatter
log_formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s [%(name)s]")
log_formatter.datefmt = "%Y/%m/%d %H:%M:%S"

# handlers
fh = logging.FileHandler(log_file)
fh.setLevel(log_level)
fh.setFormatter(log_formatter)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(log_formatter)

# ### application config ###

# slack tokens
SLK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", default="*****")
SLK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", default="*****")

# ### end of config ###

# log some useful info
logger = logging.getLogger(__name__)
logger.setLevel(log_level)
logger.addHandler(ch)
logger.addHandler(fh)

_debug_msg = f"{SLK_BOT_TOKEN[-4:]=}, {SLK_APP_TOKEN[-4:]=}"
logger.debug(_debug_msg)

logger.info(f"Config completed ({DEBUG_MODE=})")

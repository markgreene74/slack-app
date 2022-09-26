import logging
import re
import bot.config as cfg
import bot.fo76 as fo76
from slack_bolt import App

# message patterns
pattern_fo76 = re.compile(r"[fF][oO]76|\!76|^76$")
pattern_hello = re.compile(r"[hH](i|ello|ey)")

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)

app = App(token=cfg.SLK_BOT_TOKEN)
logger.debug("Bolt started")


# reply to messages containing different patterns
@app.message(pattern_hello)
def message_hello(message, say):
    logger.info(f"hello requested by user: {message['user']}")
    say(f"Hey there <@{message['user']}>!")


@app.message(pattern_fo76)
def message_fo76(message, say):
    logger.info(f"FO76 requested by user: {message['user']}")
    say(f"FO76 silo codes:\n{fo76.get_codes()}")

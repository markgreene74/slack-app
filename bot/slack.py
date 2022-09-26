import logging
import bot.config as cfg
from slack_bolt import App

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)

app = App(token=cfg.SLK_BOT_TOKEN)
logger.debug("Bolt started")


# reply to messages containing "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    logger.info(f"hello message - user {message['user']}")
    say(f"Hey there <@{message['user']}>!")

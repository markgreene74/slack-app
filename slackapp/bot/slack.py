import logging
import re

from slack_bolt import App

import slackapp.api_interface.api_interface as api
import slackapp.bot.config as cfg
import slackapp.bot.fo76 as fo76
from slackapp.bot.messages import find_reply, regex_from_file

# message patterns
pattern_fo76 = re.compile(r"[fF][oO]76|\!76|^76$")

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)
logger.addHandler(cfg.fh)

app = App(token=cfg.SLK_BOT_TOKEN)
logger.debug("Bolt started")


#  ### messages ###


@app.message(regex_from_file("hello_messages"))
def message_hello(message, say):
    logger.info(f"hello requested by user: {message['user']}")
    reply = find_reply(message["text"], "hello_messages")
    say(f"{reply} <@{message['user']}>!")


@app.message(pattern_fo76)
def message_fo76(message, say):
    logger.info(f"FO76 requested by user: {message['user']}")
    say(f"FO76 silo codes:\n{fo76.get_codes()}")


@app.message(re.compile(r"debug"))
def message_debug(say, context):
    # regular expression matches are inside of context.matches
    # say(f"{context['matches']}")
    if logger.level == logging.DEBUG:
        say(f"{type(context)}\n\n{context.items()}\n\n{context.keys()}")
    else:
        say(":sleeping:")


#  ### commands ###


@app.command("/api")
def command_api(ack, say, command):
    logger.info(
        f"API query requested by user: {command['user_name']} ({command['user_id']}) in the channel {command['channel_name']} ({command['channel_id']})"
    )
    logger.info(f"{command['text']=}")
    # Acknowledge command request
    ack()
    if len(command["text"].split()) > 1:
        response = "Invalid URL"
    else:
        response = api.query(command["text"])
    say(f"{response}")


#  ### events ###


@app.event("message")
def event_message_handler(body):
    if body["event"].get("subtype") == "message_deleted":
        _message_deleted = body["event"]["previous_message"]
        _id = _message_deleted.get("user") or _message_deleted.get("bot_id")
        _type = _message_deleted.get("type")
        _text = _message_deleted.get("text")
        logger.info(f"{_type} from {_id} was deleted - Text: {_text}")
    else:
        logger.info(body)

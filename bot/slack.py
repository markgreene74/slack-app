import logging
import re
import bot.config as cfg
import bot.fo76 as fo76
import api_interface.api_interface as api
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


@app.command("/api")
def repeat_text(ack, say, command):
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


@app.message(re.compile(r"debug"))
def test_regex(say, context):
    # regular expression matches are inside of context.matches
    # say(f"{context['matches']}")
    say(f"{type(context)}\n\n{context.items()}\n\n{context.keys()}")


# handle message deletion
@app.event("message")
def handle_message_events(body):
    if body["event"].get("subtype") == "message_deleted":
        _message_deleted = body["event"]["previous_message"]
        _id = _message_deleted.get("user") or _message_deleted.get("bot_id")
        _type = _message_deleted.get("type")
        _text = _message_deleted.get("text")
        logger.info(f"{_type} from {_id} was deleted - Text: {_text}")
    else:
        logger.info(body)

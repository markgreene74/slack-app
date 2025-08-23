import functools
import logging

from prometheus_client import Counter, Info, Summary, start_http_server

import slackapp.bot.config as cfg

MESSAGE_TYPE_MAPPING = {"hello": 1, "ciao": 2, "salut": 3, "hallo": 4, "ola": 5}

# Metrics
INFO = Info("slackapp_build_version", "Description of build_version")
REPLIES = Counter("slackapp_replies", "Description of replies")
MTYPE = Counter(
    "slackapp_message_type",
    "Description of message_type",
    ["message_type", "something_else"],
)

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)
logger.addHandler(cfg.fh)


def start_metrics():
    logger.info("Starting metrics")
    # Define some basic application info.
    INFO.info({"app_name": "slack_app", "version": "1.2.3"})
    # Start up the server to expose the metrics.
    start_http_server(8008)


def count_replies(func):
    logger.info("Initialising counting decorator")

    @functools.wraps(func)
    def wrapper_count_replies(*args, **kwargs):
        logger.info("Incrementing counter")
        REPLIES.inc()
        return func(*args, **kwargs)

    return wrapper_count_replies


def message_type(reply):
    match reply:
        case "Hey there":
            _type = "hello"
        case "Ciao" | "Buon giorno" | "Buona sera":
            _type = "ciao"
        case "Salut":
            _type = "salut"
        case "Hallo":
            _type = "hallo"
        case "Olá" | "Bom dia" | "Boa noite":
            _type = "ola"
        case _:
            _type = "undefined"

    logger.info("message type %s %s", _type, MESSAGE_TYPE_MAPPING.get(_type))
    MTYPE.labels(
        message_type=MESSAGE_TYPE_MAPPING.get(_type, 0), something_else=0
    ).inc()

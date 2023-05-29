import json
import logging
import re
from string import punctuation
from typing import Pattern

import bot.config as cfg

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)


def load_data(file_name: str) -> dict:
    file_full_path = f"bot/data/{file_name}.json"
    logger.info(f"loading data from {file_full_path}")
    with open(file_full_path) as f:
        data = f.read()
    return json.loads(data)


def find_reply(message: str, file_name: str) -> str:
    data = load_data(file_name)
    logger.info(
        f'loaded {file_name} data, now trying to match "{message}" and find a reply'
    )

    message_trimmed = (
        message.lower().replace(" ", "").translate(str.maketrans("", "", punctuation))
    )
    logger.debug(f"{message=}, {message_trimmed=}")

    for key, response in data.items():
        logger.debug(f"{key=}, {response=}")
        if message_trimmed in key:
            return response

    return "I didn't catch that!"


def regex_from_file(file_name: str) -> Pattern[str]:
    data = load_data(file_name)
    logger.info(f"loaded {file_name} data, now creating a regex pattern")
    all_keys = []
    for key in data.keys():
        all_keys.append(key)
    all_keys_str = "|".join(all_keys)
    logger.debug(f"extracted {len(all_keys)} keys: {all_keys_str=}")
    return re.compile(all_keys_str)

import json
import re


def load_data() -> dict:
    with open("bot/data/messages.json") as f:
        data = f.read()
    return json.loads(data)


def find_reply(message: str) -> str:
    data = load_data()
    for key, response in data.items():
        if message.lower() in key:
            return response
    return "I didn't catch that!"


def messages_regex() -> str:
    data = load_data()
    all_keys = []
    for key in data.keys():
        all_keys.append(key)
    all_keys_str = "|".join(all_keys)
    return re.compile(all_keys_str)

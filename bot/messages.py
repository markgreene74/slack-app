import json
import re
from typing import Pattern


def load_data(file_name: str) -> dict:
    file_full_path = f"bot/data/{file_name}.json"
    with open(file_full_path) as f:
        data = f.read()
    return json.loads(data)


def find_reply(message: str, file_name: str) -> str:
    data = load_data(file_name)
    for key, response in data.items():
        if message.lower() in key:
            return response
    return "I didn't catch that!"


def regex_from_file(file_name: str) -> Pattern[str]:
    data = load_data(file_name)
    all_keys = []
    for key in data.keys():
        all_keys.append(key)
    all_keys_str = "|".join(all_keys)
    return re.compile(all_keys_str)

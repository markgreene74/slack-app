import logging
import requests

import bot.config as cfg

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)


def query(url):
    if (not url.startswith("http://")) and (not url.startswith("https://")):
        url = f"http://{url}"

    response = requests.get(url)
    logger.info(f"{response.status_code}")
    return f"{url}: {response.text}"

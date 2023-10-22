import logging
import os
import re
from datetime import datetime

import requests

# needed to run fo76 standalone/manually
# ugly, but it works
try:
    import slackapp.bot.config as cfg
except ModuleNotFoundError:
    import config as cfg

FILENAME = "fo76"
DIRNAME = os.path.join("bot", ".tmp_data")
FILE_RELATIVE_PATH = os.path.join(DIRNAME, FILENAME)
URL = "https://www.falloutbuilds.com"

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
logger.addHandler(cfg.ch)
logger.addHandler(cfg.fh)


def check_data_dir():
    os.makedirs(DIRNAME, exist_ok=True)


def _needs_updating():
    if not os.path.isfile(FILE_RELATIVE_PATH):
        logger.debug(f"{FILE_RELATIVE_PATH} does not exist, triggering an update")
        return True

    modified = datetime.fromtimestamp(os.path.getmtime(FILE_RELATIVE_PATH))
    days_old = (datetime.today() - modified).days
    logger.info(f"FO76 last checked: {modified.date()=}")

    return True if days_old >= 5 else False


def get_updates(save_file=True):
    logger.debug("Fetching data")

    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    response = requests.get(URL, headers={"User-Agent": ua})
    logger.debug(f"{response.status_code=}")
    content = str(response.content)

    silos = re.findall(r"\>(ALPHA|BRAVO|CHARLIE)\<", content)
    codes = re.findall(r"\>(\d{3}\s{1}\d{2}\s{1}\d{3})\<", content)

    # >>> silos
    # ['ALPHA', 'BRAVO', 'CHARLIE']
    # >>> codes
    # ['841 38 947', '676 23 748', '512 39 897']
    # >>> list(zip(silos, codes))
    # [('ALPHA', '841 38 947'), ('BRAVO', '676 23 748'), ('CHARLIE', '512 39 897')]

    logger.debug(f"Found: {silos=} {codes=}")

    s_c_list = [f"{s}:{c}" for s, c in list(zip(silos, codes))]
    file_content = "\n".join(s_c_list)
    logger.debug(f"{file_content=}")

    if save_file:
        check_data_dir()
        with open(FILE_RELATIVE_PATH, "w") as f:
            f.write(file_content)
        logger.info(f"Updated {FILE_RELATIVE_PATH}")

    return file_content


def get_codes():
    logger.debug("Checking if an update is needed")
    if _needs_updating():
        logger.debug("Updating ...")
        return get_updates()
    else:
        logger.debug("An update is NOT needed")
        with open(FILE_RELATIVE_PATH) as f:
            data = f.read()
        return data


if __name__ == "__main__":
    logger.info("Fetching FO76 Silo codes ...")
    print(get_updates(save_file=False))

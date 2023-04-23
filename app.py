import logging

from slack_bolt.adapter.socket_mode import SocketModeHandler

import bot.config as cfg
import bot.slack as slk

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(cfg.log_level)
    logger.addHandler(cfg.ch)

    logger.info(
        f"Starting slack-app (log level: {logging.getLevelName(logger.getEffectiveLevel())})"
    )

    SocketModeHandler(slk.app, cfg.SLK_APP_TOKEN).start()

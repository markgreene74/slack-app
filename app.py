import logging

import bot.config as cfg
import bot.slack as slk

from slack_bolt.adapter.socket_mode import SocketModeHandler


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(cfg.log_level)
    logger.addHandler(cfg.ch)

    logger.info(
        f"Starting slack-app (log level: {logging.getLevelName(logger.getEffectiveLevel())})"
    )

    SocketModeHandler(slk.app, cfg.SLK_APP_TOKEN).start()

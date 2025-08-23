import logging

from slack_bolt.adapter.socket_mode import SocketModeHandler

import slackapp.bot.config as cfg
import slackapp.bot.slack as slk
import slackapp.metrics.metrics as mts

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(cfg.log_level)
    logger.addHandler(cfg.ch)
    logger.addHandler(cfg.fh)

    logger.info(
        f"Starting slack-app (log level: {logging.getLevelName(logger.getEffectiveLevel())})"
    )

    mts.start_metrics()

    SocketModeHandler(slk.app, cfg.SLK_APP_TOKEN).start()

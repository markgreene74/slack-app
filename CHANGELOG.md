## [v0.6](https://github.com/markgreene74/slack-app/releases/tag/v0.6) (2024-05-06)

Default to building a `deploy` image instead of a `dev` image.

## [v0.5](https://github.com/markgreene74/slack-app/releases/tag/v0.5) (2024-05-06)

Maintenance release, bump up the Python version (`3.10` -> `3.12`) and Debian base image (`bullseye` -> `bookworm`).

## [v0.2](https://github.com/markgreene74/slack-app/releases/tag/v0.2) (2023-05-29)

With this release we introduce a better system to handle messages and replies.

The messages/replies are now loaded from `JSON` file(s) located inside the directory [`bot/data`](bot/data). To add a new collection of messages and replies:
- create a new messages file in `bot/data`
- add a new handler function in `slack.py`

Example:

- `new_messages.json`
  ```json
  {
      "foo|[fF][oO][oO]|bar|[bB][aA][rR]": "Hey there! The message is either 'foo' or 'bar'",
      "foobarbaz|[fF][oO][oO][ ]*[bB][aA][rR][ ]*[bB][aA][zZ]": "The message is 'foo bar baz'"
  }
  ```
- handler
  ```python
  @app.message(regex_from_file("new_messages"))
  def message_new(message, say):
      logger.info(f"Useful log goes here, for example - user: {message['user']}")
      reply = find_reply(message["text"], "new_messages")
      say(f"This is the reply: {reply}")
  ```

**IMPORTANT NOTES**
- the `JSON` file must contain each keyword both as lower case, stripped (no spaces) string (`foo`) and the corresponding regex (`[fF][oO][oO]`), separated by `|`
- it is possible to add multiple keywords that trigger the same reply using the same pattern
- to catch messages that contain spaces, add `[ ]*` to the regex section

### New Features
* handle more complex messages that are loaded from `JSON` file(s)

### Other Changes
* better testing, introduced a `test_data` directory that matches the `data` directory

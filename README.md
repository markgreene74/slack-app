# slack-app

TOC
- [pre-work](#pre-work)
- [pre-commit](#pre-commit)
- [github workflows](github-workflows)
- [development](#development)
- [test](#test)
- [reference](#reference)

## pre-work

on CodeAnywhere:
```
# update pyenv
cd /home/cabox/.pyenv/plugins/python-build/../.. && git pull && cd -

# install liblzma
sudo apt update
sudo apt install lzma-dev liblzma-dev

# install the latest 3.9.x release
pyenv install 3.9.14

# create a virtual environment and activate it
pyenv virtualenv 3.9.14 slack-app-venv
pyenv activate slack-app-venv
```

## pre-commit

TBA

## github workflows

TBA

## development

TBA

## test

TBA

## reference

- [PyPI - slack-sdk](https://pypi.org/project/slack-sdk/)
- [PyPI - slack-bolt](https://pypi.org/project/slack-bolt/)
- [GitHub - Slack Developer Kit for Python](https://github.com/slackapi/python-slack-sdk)
- [Slack - api](https://api.slack.com/)
- [Slack - apps](https://api.slack.com/apps)
- [Slack Bolt - Getting started](https://slack.dev/bolt-python/tutorial/getting-started)
- [Slack - Block Kit Builder](https://app.slack.com/block-kit-builder)

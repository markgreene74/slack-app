# slack-app

TOC
- [pre-work](#pre-work)
  - [pyenv](#pyenv)
  - [pre-commit](#pre-commit)
  - [github workflows](#github-workflows)
- [usage](#usage)
- [development](#development)
- [test](#test)
- [with docker](#with-docker)
- [reference](#reference)

## pre-work

### pyenv:

```shell
# update pyenv
cd ${PYENV_ROOT}/plugins/python-build/../.. && git pull && cd -

# install liblzma
sudo apt update
sudo apt install liblzma-dev

# install the latest 3.10.x release
pyenv install 3.10.11

# create a virtual environment and activate it
pyenv virtualenv 3.10.11 slack-app-venv
pyenv activate slack-app-venv
```

### pre-commit

`pre-commit`, `black`, `pylint` and `flake8` are included in `requirements-dev.txt`.

Make sure `pre-commit` is installed:
```shell
pre-commit --version
```

Set up the git hook scripts:
```shell
pre-commit install
```

First run `pre-commit` on all files:
```shell
pre-commit run --all-files
```

### github workflows

TBA

## usage

Export the environment variables:
```shell
source ~/.secrets/ENV_VARS
```

Run `app.py`:
```shell
export SLACK_BOT_TOKEN; export SLACK_APP_TOKEN; python app.py
```

### force an update of the FO76 Silo codes

```shell
python bot/fo76.py
```

## development

Run `app.py` in debug mode:
```shell
export SLACK_BOT_TOKEN; export SLACK_APP_TOKEN; SLACK_BOT_DEBUG=true; python app.py
```

## test

TBA

## with docker

### run the application

```shell
docker build --target deploy -t slack-app .
docker run --env-file ~/.secrets/ENV_VARS --rm slack-app
```

### run the tests

```shell
docker build --target test -t slack-app-test .
docker run --rm slack-app-test
```

run the test container interactively

```shell
docker run -it --rm slack-app-test bash
```

### start the container for development

```shell
docker build --target dev -t slack-app-dev .
docker run --env-file ~/.secrets/ENV_VARS -it --rm slack-app-dev
```

## reference

- PyPI
  - [PyPI - slack-sdk](https://pypi.org/project/slack-sdk/)
  - [PyPI - slack-bolt](https://pypi.org/project/slack-bolt/)
- github
  - [GitHub - Slack Developer Kit for Python](https://github.com/slackapi/python-slack-sdk)
- slack.com
  - [Slack - api](https://api.slack.com/)
  - [Slack - apps](https://api.slack.com/apps)
  - [Slack - Block Kit Builder](https://app.slack.com/block-kit-builder)
- slack.dev/bolt-python
  - [Slack Bolt - Getting started](https://slack.dev/bolt-python/tutorial/getting-started)
  - [Slack Bolt - concepts](https://slack.dev/bolt-python/concepts)

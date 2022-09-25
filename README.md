# slack-app

TOC
- [pre-work](#pre-work)
  - [pyenv](#pyenv)
  - [pre-commit](#pre-commit)
  - [github workflows](github-workflows)
- [usage](#usage)
- [development](#development)
- [test](#test)
- [reference](#reference)

## pre-work

### pyenv:

```
# update pyenv
cd ${PYENV_ROOT}/plugins/python-build/../.. && git pull && cd -

# NOTE: on codeanywhere PYENV_ROOT is not defined, just use:
# cd /home/cabox/.pyenv/plugins/python-build/../.. && git pull && cd -

# install liblzma
sudo apt update
sudo apt install liblzma-dev

# install the latest 3.9.x release
pyenv install 3.9.14

# create a virtual environment and activate it
pyenv virtualenv 3.9.14 slack-app-venv
pyenv activate slack-app-venv
```

### pre-commit

`pre-commit`, `black`, `pylint` are included in `requirements-dev.txt`.

Make sure `pre-commit` is installed:
```
pre-commit --version
```

Set up the git hook scripts:
```
pre-commit install
```

First run `pre-commit` on all files:
```
pre-commit run --all-files
```

### github workflows

TBA

## usage

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

https://slack.dev/bolt-python/tutorial/getting-started

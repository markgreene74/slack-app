| [![CodeQL](https://github.com/markgreene74/slack-app/actions/workflows/codeql.yml/badge.svg)](https://github.com/markgreene74/slack-app/actions/workflows/codeql.yml) | [![Snyk](https://github.com/markgreene74/slack-app/actions/workflows/snyk.yml/badge.svg)](https://github.com/markgreene74/slack-app/actions/workflows/snyk.yml) | [![Tests](https://github.com/markgreene74/slack-app/actions/workflows/python-run-tests.yml/badge.svg)](https://github.com/markgreene74/slack-app/actions/workflows/python-run-tests.yml) |
| --- | --- | --- |

# slack-app

- [quick start](#quick-start)
  - [pre-work](#pre-work)
  - [run slack-app](#run-slack-app)
  - [run slack-app with docker](#run-slack-app-with-docker)
- [github](#github)
  - [codespaces](#codespaces)
  - [actions](#actions)
- [development](#development)
- [deploy slack-app](#deploy-slack-app)
- [reference](#reference)
- [misc](#misc)

## quick start

### pre-work

- create the `ENV_VARS` file containing the `SLACK_BOT_TOKEN` and  `SLACK_APP_TOKEN`
    ```
    SLACK_BOT_TOKEN=xoxb-<REPLACEME>
    SLACK_APP_TOKEN=xapp-<REPLACEME>
    ```
- install the requirements and activate the virtual environment, see the [pre-work section in docs/development.md](docs/development.md#pre-work) for more details

### run slack-app

- export the environment variables
    ```shell
    source ~/.secrets/ENV_VARS
    ```
- run `app.py`
    ```shell
    export PYTHONPATH=.; export SLACK_BOT_TOKEN; export SLACK_APP_TOKEN; python slackapp/app.py
    ```

### run slack-app with docker

- pull the image locally
    ```shell
    docker pull ghcr.io/markgreene74/slack-app:latest
    ```
- start the container
    ```shell
    docker run \
        --env-file ~/.secrets/ENV_VARS \
        --rm \
        slack-app
    ```

## github

### codespaces

A [devcontainer.json](.devcontainer/devcontainer.json) file has been added for custom Codespaces which include `pre-commit` hooks. See the GitHub documentation about [creating a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) to work on `slack-app`.

### actions

Multiple GitHub Actions (workflow) are configured to ensure automated testing, linting and security scans ([Snyk](https://snyk.io/)).

Actions:

|                                                              | on `push`            | on PR  | schedule | run manually |
|--------------------------------------------------------------|----------------------|--------|----------|--------------|
| [CodeQL](.github/workflows/codeql.yml)                       | `main`               | `main` | Y        | N            |
| [Build and publish](.github/workflows/docker-publish.yml)    | `main`               | N      | N        | Y            |
| [Run tests and lint](.github/workflows/python-run-tests.yml) | `main`, `feature/**` | `main` | N        | Y            |
| [Release](.github/workflows/release.yml)                     | `main`               | `main` | N        | N            |
| [Snyk](.github/workflows/snyk.yml)                           | `main`               | `main` | N        | N            |

## development

See: [docs/development.md](docs/development.md)

## deploy slack-app

See: [docs/deployment.md](docs/deployment.md)

## miscellanea

See: [docs/miscellanea.md](docs/miscellanea.md)

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

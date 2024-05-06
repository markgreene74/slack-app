# development

- [pre-work](#pre-work)
  - [create a virtual environment](#create-a-virtual-environment)
  - [pyenv/pyenv-virtualenv](#pyenvpyenv-virtualenv)
  - [activate the virtual environment](#activate-the-virtual-environment)
  - [install the requirements](#install-the-requirements)
  - [install the pre-commit hooks](#install-the-pre-commit-hooks)
- [start slack-app in debug mode](#start-slack-app-in-debug-mode)
- [tests](#tests)
  - [run the tests](#run-the-tests)
  - [run the tests with docker](#run-the-tests-with-docker)
- codespaces (TBA)
- gitpod (TBA)

## pre-work

### create a virtual environment

While not strictly needed, it is a good idea to create a virtual environment to run and develop `slack-app`. See the Python documentation for more details on [Creating a virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

It is possible to use `pyenv` and `pyenv-virtualenv` to easily create&manage different Python versions and virtual environments.

#### pyenv/pyenv-virtualenv

See the [pyenv documentation](https://github.com/pyenv/pyenv#installation) and the [pyenv-virtualenv documentation](https://github.com/pyenv/pyenv-virtualenv#installation) for more details about the installation.

```shell
# update pyenv
cd $(pyenv root) && git pull && cd -
# pyenv-virtualenv
cd $(pyenv root)/plugins/pyenv-virtualenv && git pull && cd -

# install liblzma
sudo apt update && \
    sudo apt install liblzma-dev

# find the latest 3.12.x version available in pyenv
export PY_VERSION=$(pyenv install -l | grep "^\s*3.12" | tail -n 1 | awk '{print $1}') && \
    echo $PY_VERSION

# install the latest 3.12.x release
pyenv install $PY_VERSION

# create a virtual environment
pyenv virtualenv $PY_VERSION slack-app-venv
```

### activate the virtual environment

See the Python documentation for more details on [Activating a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment).

If using `pyenv` and `pyenv-virtualenv` run

```shell
pyenv activate slack-app-venv
```

### install the requirements

```shell
pip install -r requirements-dev.txt
```

`pre-commit`, `black`, `pylint` and `flake8` are included in `requirements-dev.txt`.

### install the pre-commit hooks

- make sure `pre-commit` is installed
    ```shell
    pre-commit --version
    ```
- install `pre-commit` to set up the git hook scripts
    ```shell
    pre-commit install
    ```

See also [the pre-commit tips section in miscellanea.md](miscellanea.md#pre-commit-tips).

## start slack-app in debug mode

Export the environment variables
```shell
source ~/.secrets/ENV_VARS
```

Run `app.py` in debug mode
```shell
export SLACK_BOT_DEBUG=true && \
    export PYTHONPATH=.; \
    export SLACK_BOT_TOKEN; export SLACK_APP_TOKEN; python app.py
```

To switch off debug mode unset the env variable
```shell
unset SLACK_BOT_DEBUG && \
    export PYTHONPATH=.; \
    export SLACK_BOT_TOKEN; export SLACK_APP_TOKEN; python app.py
```

## tests

### run the tests

GH Actions is configured to run `pytest` on `push` to the `main` branch and on PRs opened against the `main` branch.

It is possible to [run tests with docker](#run-the-tests-with-docker), or manually like in this example
```
(slack-app-venv) (...):~/github/slack-app$ pytest
========================= test session starts =========================
platform linux -- Python 3.12.3, pytest-7.3.1, pluggy-1.0.0
rootdir: /home/user/github/slack-app
collected 1 item

tests/test_dummy.py .                                           [100%]

========================== 1 passed in 0.01s ==========================
(slack-app-venv) (...):~/github/slack-app$
```

Note that outside a virtual environment it will be needed to add `PYTHONPATH` explicitly
```shell
export PYTHONPATH=. ; pytest
```

### run the tests with docker

```shell
docker build --target test -t slack-app-test .
docker run --rm slack-app-test
```

Run the test container interactively

```shell
docker run -it --rm slack-app-test bash
```

### start the container for development

```shell
docker build --target dev -t slack-app-dev .
docker run \
    --env-file ~/.secrets/ENV_VARS \
    -it \
    --rm \
    slack-app-dev
```

If you wish to export the log files

```shell
docker build --target deploy -t slack-app .
mkdir -p ./logs
docker run \
    --env-file ~/.secrets/ENV_VARS \
    -it \
    --rm \
    --mount type=bind,source="$(pwd)"/logs,target=/var/log/slack-app \
    slack-app
```

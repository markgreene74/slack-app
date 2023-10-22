# syntax=docker/dockerfile:1

# Main application directory
ARG APP_DIRECTORY=slackapp

FROM python:3.10-slim-bullseye AS base
RUN apt-get update && \
    apt-get install liblzma-dev -y
RUN adduser --disabled-login --gecos "" slack-app
RUN mkdir -p /var/log/slack-app && \
    chown slack-app:slack-app /var/log/slack-app
RUN pip install --upgrade setuptools pip


FROM base AS deploy
USER slack-app
ENV PATH="${PATH}:/home/slack-app/.local/bin/"
WORKDIR /usr/src/app
COPY --chown=slack-app:slack-app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --quiet
COPY --chown=slack-app:slack-app $APP_DIRECTORY ./
CMD ["python", "app.py"]


FROM base AS test
USER slack-app
ENV PATH="${PATH}:/home/slack-app/.local/bin/"
WORKDIR /usr/src/app
COPY --chown=slack-app:slack-app requirements*.txt .
RUN pip install --no-cache-dir -r requirements-test.txt --quiet
COPY --chown=slack-app:slack-app $APP_DIRECTORY ./
CMD ["pytest"]


FROM test AS dev
USER root
RUN apt-get update && \
    apt-get install git -y
USER slack-app
ENV PATH="${PATH}:/home/slack-app/.local/bin/"
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements-dev.txt --quiet && \
    pip --disable-pip-version-check list --outdated --format=json
# pip --disable-pip-version-check list --outdated --format=json | python -c "import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))"
RUN git init . && \
    pre-commit --version && \
    pre-commit install
CMD ["/bin/bash"]

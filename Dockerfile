# syntax=docker/dockerfile:1

FROM python:3.14.0a3-slim-bookworm AS base
RUN apt-get update && \
    apt-get install liblzma-dev -y
RUN adduser --disabled-login --gecos "" slack-app
RUN mkdir -p /var/log/slack-app && \
    chown slack-app:slack-app /var/log/slack-app
RUN pip install --upgrade setuptools pip


FROM base AS test
USER slack-app
ENV PATH="${PATH}:/home/slack-app/.local/bin/"
WORKDIR /usr/src/app
COPY --chown=slack-app:slack-app requirements*.txt .
RUN pip install --no-cache-dir -r requirements-test.txt --quiet
COPY --chown=slack-app:slack-app . .
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
ENV PYTHONPATH "${PYTHONPATH}:/user/src/app"
CMD ["/bin/bash"]


FROM base AS deploy
USER slack-app
ENV PATH="${PATH}:/home/slack-app/.local/bin/"
WORKDIR /usr/src/app
COPY --chown=slack-app:slack-app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --quiet
COPY --chown=slack-app:slack-app . .
ENV PYTHONPATH "${PYTHONPATH}:/user/src/app"
CMD ["python", "slackapp/app.py"]

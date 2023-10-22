#!/usr/bin/env bash

set -euo pipefail

if [[ $# -eq 1 ]] && [[ $1 == "--with-watchtower" ]]
then
    # TODO add support for watchtower
    echo "${1}"
fi

if ! { [[ $(pwd) == *"slack-app"* ]] && [[ $(ls Dockerfile) ]]; }
then
  echo "The script was called from the wrong directory! Make sure to be in the slack-app directory."
  exit 1
fi


# make sure the logs directory is present
mkdir -p ./logs

# build the docker image
docker build --target deploy -t slack-app .

# alternatively pull the image from the GitHub registry
# docker pull ghcr.io/markgreene74/slack-app:latest

# run slack-app
docker run \
    -d \
    --env-file ~/.secrets/ENV_VARS \
    --rm \
    --mount type=bind,source="$(pwd)"/logs,target=/var/log/slack-app \
    slack-app

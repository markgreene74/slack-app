#!/usr/bin/env bash

set -euo pipefail

### variables

APP_NAME="slack-app"
SCRIPT_NAME=$(basename -- "${0}")
HELP_USAGE="${SCRIPT_NAME} [--build|build] [--help|help] [--with-watchtower|with-watchtower]

--build|build: build the Docker image locally
--help|help: print this help and exit
--with-watchtower|with-watchtower: start Watchtower to automatically update and restart the container when a new version is available
"
HELP_MSG="Helper script to start ${APP_NAME}

Usage:
${HELP_USAGE}"

# defaults
BUILD_LOCALLY=false
WITH_WATCHTOWER=false

### pre-flight

if ! { [[ $(pwd) == *"slack-app"* ]] && [[ $(ls Dockerfile) ]]; }
then
  echo "The script ${0} was called from the wrong directory! Make sure to be in the 'slack-app' directory."
  exit 1
fi

# make sure the logs directory is present
mkdir -p ./logs

### check the args

while [[ $# -gt 0 ]]
do
    case "$1" in
        --help|help) echo "${HELP_MSG}"
                     exit 0
            ;;
        --build|build) echo "--build selected"
                       BUILD_LOCALLY=true
            ;;
        --with-watchtower|with-watchtower) echo "--watchtower selected"
                                           WITH_WATCHTOWER=true
            ;;
        --*) echo "option $1 not recognised"
             exit 1
            ;;
        *) echo "argument $1 not recognised"
           exit 1
            ;;
    esac
    shift
done

### decide which image will be used

if $BUILD_LOCALLY
then
  # build the docker image locally
  docker build --target deploy -t slack-app .
else
  # pull the image from the GitHub registry
  docker pull ghcr.io/markgreene74/slack-app:latest
fi

if $WITH_WATCHTOWER
then
  # start Watchtower
  # TODO add support for watchtower
  echo "start Watchtower TBA"
fi

### start slack-app

docker run \
    -d \
    --env-file ~/.secrets/ENV_VARS \
    --rm \
    --mount type=bind,source="$(pwd)"/logs,target=/var/log/slack-app \
    slack-app

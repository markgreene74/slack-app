#!/usr/bin/env bash

set -euo pipefail

### variables

APP_NAME="slack-app"
ENV_FILE="${HOME}/.secrets/ENV_VARS"
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

### functions

stop_container_if_running () {
# check if a container is running and stop it
CONTAINER_ID=$(docker ps --filter "name=${1}" --filter "status=running" --quiet)
if [[ "${CONTAINER_ID}" ]]
then
  echo "A ${APP_NAME} container is already running. Stopping ${CONTAINER_ID} ..."
  docker stop "${CONTAINER_ID}"
fi
}

### pre-flight

if ! { [[ $(pwd) == *"slack-app"* ]] && [[ $(ls Dockerfile) ]]; }
then
  echo "The script ${SCRIPT_NAME} was called from the wrong directory! Make sure to be in the 'slack-app' directory."
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
        --*) echo "Option $1 not recognised"
             exit 1
            ;;
        *) echo "Argument $1 not recognised"
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
  # see https://github.com/containrrr/watchtower
  stop_container_if_running watchtower
  echo "Starting watchtower"
  docker run -d \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --name watchtower \
    containrrr/watchtower
fi

### start slack-app

# stop the old container if needed
stop_container_if_running "${APP_NAME}"
# start a new container
echo "Starting ${APP_NAME}"
docker run \
    -d \
    --env-file "${ENV_FILE}" \
    --rm \
    --mount type=bind,source="$(pwd)"/logs,target=/var/log/slack-app \
    --name "${APP_NAME}" \
    "${APP_NAME}"

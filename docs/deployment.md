# deployment

- [make the image available locally](#make-the-image-available-locally)
- [start slack-app](#start-slack-app)

## make the image available locally

- build the docker image
    ```shell
    docker build --target deploy -t slack-app .
    ```
- alternatively pull the image from `ghcr`
    ```shell
    docker pull ghcr.io/markgreene74/slack-app:latest
    ```

# start slack-app

- create a directory on the host to export the logs
    ```shell
    mkdir -p ./logs
    ```
- start the container
    ```shell
    docker run \
        -d \
        --env-file ~/.secrets/ENV_VARS \
        --rm \
        --mount type=bind,source="$(pwd)"/logs,target=/var/log/slack-app \
        slack-app
    ```

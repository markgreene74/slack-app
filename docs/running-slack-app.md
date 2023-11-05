# running slack-app

- [run manually](#run-manually)
- [use the helper script](#use-the-helper-script)

## run manually

### make the image available locally

- build the docker image
    ```shell
    docker build --target deploy -t slack-app .
    ```
- alternatively pull the image from `ghcr`
    ```shell
    docker pull ghcr.io/markgreene74/slack-app:latest
    ```

### start the application

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
        --name slack-app \
        slack-app
    ```

## use the helper script

- make sure to be in the project main directory (`slack-app`) and run
    ```shell
    scripts/run-in-docker.sh
    ```

Optional arguments for `run-in-docker.sh`:
- `--build`|`build`: build the Docker image locally instead of pulling it from `ghcr.io/markgreene74/slack-app`, default is `false`
- `--help`|`help`: print the help and exit
- `--with-watchtower`|`with-watchtower`: start Watchtower to automatically update and restart the container when a new version is available, default is `false`

To learn more about Watchtower see https://github.com/containrrr/watchtower

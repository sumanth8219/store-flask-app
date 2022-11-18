#!/usr/bin/bash

echo "Rebuilding local container"
container_id=`docker ps  | awk 'NR>1' | awk '{print $1}'`
if [[ ! -z "$container_id" ]]; then
    echo "stopping $container_id"
    docker stop $container_id
        if [[ $? != 0 ]]; then
            echo "error stopping $container_id"
            exit 1
        else
            echo "$container_id stopped successfully."
        fi
else
    echo "Starting new one"
fi

out=`docker run -d --network host -w /app -v "$(pwd):/app" $1`
if [ ! -z "$out" ]; then
    echo "new container started $out"
    log_out=`docker logs $out`
    echo "$log_out"
else
    echo "not sure what happened to $out"
fi

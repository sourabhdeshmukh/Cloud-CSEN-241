#!/bin/bash

echo `date` "[INFO] Starting the Docker Container for performing Sysbench test cases on the Container."

docker run -it --memory="2048g" --cpus="2" sourabhdeshmukh/ubuntu-sysbench:v2

if [ $? -ne 0 ]; then
    echo `date` "[ERROR] Container Failed to start."
    exit 1
else
    echo `date`"[INFO] Docker container started Successfully."
fi


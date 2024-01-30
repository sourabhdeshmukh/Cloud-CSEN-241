#!/bin/bash

echo `date` "[INFO] Starting Docker Image Build for performing sysbench test cases using custom sysbench image sourabhdeshmukh/ubuntu-sysbench:v1."

docker build -t sourabhdeshmukh/ubuntu-sysbench:v2 .

if [ $? -ne 0 ]; then
    echo `date` "[ERROR] Failed to build a Docker Image."
    exit 1
else
    echo `date`"[INFO] Docker image Built Successfully."
    echo `date`"[INFO] Not run the Docker container using command docker run -it -v ./tmp:/tmp sourabhdeshmukh/ubuntu-sysbench:v2"
fi

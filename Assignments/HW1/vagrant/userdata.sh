#!/bin/bash

apt update -y
wget -qO - https://packagecloud.io/install/repositories/akopytov/sysbench/script.deb.sh | sudo bash
sudo apt install -y sysbench
mkdir /sysbench


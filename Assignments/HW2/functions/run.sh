#!/bin/bash
faas-cli remove -f chatbot.ym
faas-cli remove -f chatbot.ym
docker rmi -f $(docker images -a -q)
faas-cli build --no-cache -f chatbot.yml
faas-cli push -f chatbot.yml
faas-cli deploy -f chatbot.yml
faas-cli deploy -f chatbot.yml

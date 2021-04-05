#! /bin/bash
#
#【build】
#
IMAGE_NAME="telegram-bot"
cd ..
sudo docker build --no-cache -t ${IMAGE_NAME} -f docker/Dockerfile . 

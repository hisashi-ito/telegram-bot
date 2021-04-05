#! /bin/bash
#
#【launch】
#
IMAGE="telegram-bot"
CONTAINER="telegram-bot-container"
sudo docker run -tid --privileged -v /data:/data --name ${CONTAINER} ${IMAGE} /sbin/init

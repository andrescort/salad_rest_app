#!/bin/ash

apk update \
        && apk add --no-cache py3-pip -y \
        && rm /etc/apk/repositories \
        && pip3 --no-cache-dir install -r requirements.txt \
        && flask run --host=0.0.0.0 --port=8080

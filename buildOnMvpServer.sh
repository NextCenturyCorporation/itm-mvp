#! /bin/bash

cd ~/github/itm-mvp
git checkout war
git pull
cd itm_server
docker build --no-cache -t itm-server .
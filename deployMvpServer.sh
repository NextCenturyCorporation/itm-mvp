#! /bin/bash
# Use https://nextcentury.atlassian.net/wiki/spaces/ITM/pages/2966978561/Setup+Local+SSH+credentials+correctly to setup ssh 
MVP_SERVER=10.216.38.88

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

ssh $MVP_SERVER docker kill itm-server; 
ssh $MVP_SERVER docker rm itm-server
ssh $MVP_SERVER docker run -d -p 8080:8080 --name itm-server itm-server


ssh $MVP_SERVER docker-compose -f /home/ec2-user/github/itm-mvp/itm_dashboard/docker_setup/docker-compose.yml down
ssh $MVP_SERVER docker-compose -f /home/ec2-user/github/itm-mvp/itm_dashboard/docker_setup/docker-compose.yml up -d

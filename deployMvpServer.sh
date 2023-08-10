#! /bin/bash
# Use https://nextcentury.atlassian.net/wiki/spaces/ITM/pages/2966978561/Setup+Local+SSH+credentials+correctly to setup ssh 
# This is the current EC2 Private IP
ITM_SERVER=
SOARTECH_SERVER=
ADEPT_SERVER=

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

deployServer() {
    ssh $ITM_SERVER docker kill itm-server; 
    ssh $ITM_SERVER docker rm itm-server;
    ssh $ITM_SERVER docker run -d -p 8080:8080 -e "ITM_HOSTNAME=$ITM_SERVER" -e "SOARTECH_HOSTNAME=$SOARTECH_SERVER" -e "ADEPT_HOSTNAME=$ADEPT_SERVER" --name itm-server itm-server;
}

deployDashbaord() {
    ssh $ITM_SERVER export ITM_HOSTNAME="$ITM_SERVER"
    ssh $ITM_SERVER docker-compose -f /home/ec2-user/github/itm-mvp/itm_dashboard/docker_setup/docker-compose.yml down
    scp ./itm_dashboard/dashboard-ui/public/configs/prod/config.js $ITM_SERVER:/home/ec2-user/github/itm-mvp/itm_dashboard/dashboard-ui/public/configs/prod/config.js
    ssh $ITM_SERVER docker-compose -f /home/ec2-user/github/itm-mvp/itm_dashboard/docker_setup/docker-compose.yml up -d
}

usage()
{
   # Display Help
   echo "Deploys resources to EC2."
   echo
   echo "Syntax: scriptTemplate [-s|d]"
   echo "options:"
   echo "s     Deploys itm-server"
   echo "d     Deploys itm-dashboard"
   echo
}

while [ "$1" != "" ]; do
    case $1 in
        -s | --server )   
            shift
            deployServer
            ;;
        -d | --dashboard )   
            shift
            deployDashbaord
            ;;
        -sd | -ds )
            shift
            deployServer 
            deployDashbaord
            ;;
        -h | --help )           
            usage
            exit
            ;;
        * )                     
            usage
            exit 1
    esac
    shift
done

        

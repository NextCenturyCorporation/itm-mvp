#! /bin/bash
# Use https://nextcentury.atlassian.net/wiki/spaces/ITM/pages/2966978561/Setup+Local+SSH+credentials+correctly to setup ssh 
MVP_SERVER=10.216.38.115

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

buildContainer() {
    BUILD_TAG=$1
    BUILD_PATH=$2

    echo "Building $BUILD_TAG with path $BUILD_PATH"
    docker build -t $BUILD_TAG $BUILD_PATH
    OLD_ID=$(ssh $MVP_SERVER "docker inspect --format {{.Id}} $BUILD_TAG 2> /dev/null || echo none")
    NEW_ID=$(docker inspect --format {{.Id}} $BUILD_TAG 2> /dev/null || echo none)
    
    if [ "$OLD_ID" == "$NEW_ID" ];
    then
        echo "    $BUILD_TAG is unchanged"
    else
        echo "    $BUILD_TAG has new image: pushing to $MVP_SERVER"
        docker save $BUILD_TAG | gzip | ssh $MVP_SERVER docker load  
    fi
}

buildContainer dashboard-ui $SCRIPT_DIR/itm_dashboard/dashboard-ui/
buildContainer dashboard-graphql $SCRIPT_DIR/itm_dashboard/node-graphql/
buildContainer itm-server $SCRIPT_DIR/itm_server/

# The following is for when the itm-server can't be built locally while on corenet, isnt necessary now
# but it does work on the machine so we will build there instead for now.
# scp ./buildOnMvpServer.sh $MVP_SERVER:/home/ec2-user/buildOnMvpServer.sh
# ssh $MVP_SERVER 'chmod +x buildOnMvpServer.sh; ./buildOnMvpServer.sh'

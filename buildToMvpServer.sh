#! /bin/bash
# Use https://nextcentury.atlassian.net/wiki/spaces/ITM/pages/2966978561/Setup+Local+SSH+credentials+correctly to setup ssh 
MVP_SERVER=10.216.38.88

CURRENT_DIR=$(pwd)
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
        docker save $BUILD_TAG | gzip | pv | ssh $MVP_SERVER docker load  
    fi
}

buildContainer dashboard-ui $SCRIPT_DIR/itm_dashboard/dashboard-ui/
buildContainer dashboard-graphql $SCRIPT_DIR/itm_dashboard/node-graphql/
buildContainer itm-server $SCRIPT_DIR/itm_server/


# ssh $MVP_SERVER docker run -d -p 8080:8080 --name itm-server itm-server:local

docker build --tag dashboard-graphql node-graphql/.
docker build --tag dashboard-ui dashboard-ui/.
cd docker_setup
docker-compose up -d
cd ..
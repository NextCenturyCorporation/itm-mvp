# dashboard-app
UI Applications. 

# Running from Docker

```
docker build --tag dashboard-graphql node-graphql/.
docker build --tag dashboard-ui dashboard-ui/.

cd docker_setup
docker-compose up -d
```

# Helpful Script to Rebuild UI

To rebuild only the dashboard-ui after making edits in that directory, from the base `itm_dashboard` directory run:
```
bash dahsboard_ui.sh
```

If you made changes to the node-graphql then you need to run the "Running from Docker" section instructions instead.
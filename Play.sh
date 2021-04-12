#! /bin/bash

sudo docker system prune --all -f

sudo docker build -t covid-dungeon .

sudo docker run -d --name python-game covid-dungeon

docker exec -it python-game /bin/bash 
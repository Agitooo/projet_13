#!/bin/bash
docker stop $(docker ps -a -q) &&
docker rm $(docker ps -a -q) &&
docker run -d --publish 80:8000 -e PORT=8000 registry.digitalocean.com/vincent/oclettings:latest
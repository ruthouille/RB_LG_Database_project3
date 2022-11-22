#!/bin/bash
#mkdir db_api
#mv db_api.py db_api
#mv my_db.py db_api
#mv requirements.txt db_api
#mv Dockerfile db_api

#docker image pull ubuntu:latest

#cd db_api
docker image build . -t db_api:1.0.1

#cd ../
docker-compose up
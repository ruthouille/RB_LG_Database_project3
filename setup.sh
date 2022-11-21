#!/bin/bash
mkdir db_api
mv db_api.py db_api
mv my_db.py db_api
mv requirements.txt db_api
mv Dockerfile db_api

cd db_api
docker image build . -t db_api:1.0.0

cd ../
docker-compose up
#!/bin/bash

#cd db_api
docker image build . -t db_api:1.0.1

#cd ../
docker-compose up
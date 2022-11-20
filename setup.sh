#!/bin/bash
docker image build . -t db_api:1.0.0
docker-compose up -d
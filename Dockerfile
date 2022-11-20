FROM ubuntu:20.04

ADD requirements.txt my_db.py db_api.py ./

RUN apt update && apt install python3-pip -y && pip3 install -r requirements.txt

EXPOSE 8000
CMD uvicorn db_api:api --host 0.0.0.0
FROM ubuntu:20.04

ADD requirements.txt db_api.py netflix_titles.csv my_db.py ./

RUN apt update && apt install python3-pip -y && pip3 install -r requirements.txt


CMD ["uvicorn", "db_api:api", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
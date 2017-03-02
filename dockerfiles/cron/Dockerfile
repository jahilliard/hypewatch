FROM ubuntu:latest
FROM python:3
MAINTAINER Justin Hilliard "justin.a.hilliard@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
COPY dependencies /dependencies
RUN pip install -r dependencies/requirements.txt
COPY src /src
COPY config_production /config
COPY __main__.py /
CMD ["python", "__main__.py"]
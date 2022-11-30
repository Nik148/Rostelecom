FROM debian:latest

RUN apt-get update && \
    apt-get install -y python3

RUN apt-get -y install python3-pip
RUN pip install virtualenv && virtualenv venv

COPY ./ .
RUN /venv/bin/pip install -r requirements.txt


##
## Base Docker image for the application
##
## All applications are suppose to work on it
##
## docker build . -t stdiff/justatest

FROM python:3.7-slim-buster

WORKDIR /tmp

## install development environment
RUN apt-get update
RUN apt-get -y install build-essential

## prepare Python environment
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

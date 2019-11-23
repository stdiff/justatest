##
## Base Docker image for the application
##
## All applications are suppose to work on it
##
## docker build . -t stdiff/justatest

FROM python:3.7-slim-buster

WORKDIR /tmp

## nameplate (just a note on the environment)
RUN echo "justatest-base" > nameplate
RUN echo date >> nameplate

## install development environment
RUN apt-get update
RUN apt-get -y install build-essential

## prepare Python environment
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

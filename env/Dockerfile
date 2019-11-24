##
## Base Docker image for the application
##
## All applications are suppose to work on it
##
## docker build . -t stdiff/justatest

FROM python:3.7-slim-buster

WORKDIR /tmp

## nameplate
## Just a note on the environment
RUN echo "justatest-base" > nameplate
RUN date >> nameplate

## Install development environment
## Needed for example pandas
RUN apt-get update
RUN apt-get -y install build-essential

## Create a working user
RUN useradd -m worker
WORKDIR /home/worker
USER worker

## Prepare Python environment
## This section must be placed at the end.
COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

## Work as an ordinary user (rather than root)
CMD ["su", "-", "worker", "-c", "/bin/bash"]
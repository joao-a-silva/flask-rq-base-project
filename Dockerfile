# VERSION  0.1.0
# AUTHOR: João A Silva
# DESCRIPTION: K10 Mercado Pago Integrator
# CREATED AT: 2021-11-10
# UPDATEd AT: 2021-11-10

# base image
FROM python:3.8-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

#ARG PYTHON_DEPS=""

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8


# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -U -r requirements.txt

EXPOSE 5050

COPY . /usr/src/app

RUN chmod +x entrypoint.sh
RUN ls -l

ENTRYPOINT /usr/src/app/entrypoint.sh

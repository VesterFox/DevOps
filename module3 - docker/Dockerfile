FROM python:3-alpine as builder
LABEL maintainer="andrey523523@gmail.com"

ARG TASK_VERSION=v3.17.0
ARG TASK_BINARY=task_linux_amd64.tar.gz

WORKDIR /dockerPractics
COPY . /dockerPractics/

RUN mkdir /build \
    && pip install pyyaml \
    && pip install jinja2 \
    && wget -O- https://github.com/go-task/task/releases/download/${TASK_VERSION}/${TASK_BINARY} \
    | tar xz -C /usr/bin
    
FROM builder as build
#WORKDIR /dockerPractics
ENV PATH="/dockerPractics:${PATH}"
RUN task build
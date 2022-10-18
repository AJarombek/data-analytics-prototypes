# Dockerfile for Python programming on Debian
# Author: Andrew Jarombek
# Date: 10/16/2022

FROM python:3.8

LABEL maintainer="andrew@jarombek.com" \
      version="1.0.0" \
      description="Dockerfile for Python programming on Debian"

RUN curl https://get.please.build > please.sh && \
    bash ./please.sh

ENV PATH="${PATH}:/root/.please/bin"

RUN pip3 install numpy numba pandas matplotlib seaborn sqlalchemy

STOPSIGNAL SIGTERM
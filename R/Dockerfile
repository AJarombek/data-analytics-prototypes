# Dockerfile for R programming on Debian
# Author: Andrew Jarombek
# Date: 10/16/2022

FROM r-base:4.2.1

LABEL maintainer="andrew@jarombek.com" \
      version="1.0.0" \
      description="Dockerfile for R programming on Debian"

RUN apt-get update \
    && apt-get install -y curl \
    && curl https://get.please.build > please.sh \
    && bash ./please.sh

ENV PATH="${PATH}:/root/.please/bin"

STOPSIGNAL SIGTERM
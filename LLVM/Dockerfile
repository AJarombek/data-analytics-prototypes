# Dockerfile for LLVM programming on Debian
# Author: Andrew Jarombek
# Date: 10/18/2022

FROM debian:bullseye-20221004-slim

LABEL maintainer="andrew@jarombek.com" \
      version="1.0.0" \
      description="Dockerfile for LLVM programming on Debian"

# Install Please Build
RUN apt-get update \
    && apt-get install -y curl \
    && curl https://get.please.build > please.sh \
    && bash ./please.sh

# Install LLVM
RUN apt-get install -y llvm-runtime

ENV PATH="${PATH}:/root/.please/bin"

STOPSIGNAL SIGTERM
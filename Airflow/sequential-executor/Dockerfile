# Dockerfile for running Airflow with a sequential executor
# Author: Andrew Jarombek
# Date: 1/11/2022

FROM apache/airflow:2.2.0-python3.8

LABEL maintainer="andrew@jarombek.com" \
      version="1.0.0" \
      description="Dockerfile for running Airflow with a sequential executor"

RUN airflow db init \
    && airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org

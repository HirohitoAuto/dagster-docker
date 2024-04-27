FROM python:3.10-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagster-webserver and dagster-daemon, and to load the DagsterInstance

RUN apt-get update && apt-get install -y git

WORKDIR /opt/dagster/app

COPY ./requirements.txt /opt/dagster/app/
RUN pip install --upgrade pip && pip install -r requirements.txt
FROM python:3.10-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagster-webserver and dagster-daemon, and to load the DagsterInstance

WORKDIR /opt/dagster/app

COPY ./requirements.txt /opt/dagster/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN mkdir /opt/dagster/app/pipeline_y
COPY ./ /opt/dagster/app/pipeline_y

ENV HACKERNEWS_NUM_DAYS_WINDOW 1

# Run dagster gRPC server on port 4000

EXPOSE 4047

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4047", "-m", "pipeline_y"]

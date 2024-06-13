FROM python:3.10-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagster-webserver and dagster-daemon, and to load the DagsterInstance

RUN apt-get update && apt-get install -y git

WORKDIR /opt/dagster/app

COPY ./requirements.txt /opt/dagster/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /opt/dagster/app/pipeline_dbt/jaffle_shop/jaffle_dagster

EXPOSE 4094

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4094", "-m", "jaffle_dagster"]
